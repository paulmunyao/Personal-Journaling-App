from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncDate
from datetime import datetime, timedelta
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from user_entry.models import JournalEntry
from user_entry.api.serializers import JournalEntrySerializer, CategorySerializer


class JournalEntryViewSet(viewsets.ModelViewSet):

    @action(detail=False, methods=["get"])
    def summary(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        period = request.query_params.get("period")

        if not start_date or not end_date:
            return Response(
                {"error": "Start and end date are both required"}, status=400
            )

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD."}, status=400
            )

        entries = JournalEntry.objects.filter(
            user=request.user, created_at_date_range=[start_date, end_date]
        )

        if period == "day":
            trunc_func = TruncDate("created_at")
        elif period == "week":
            trunc_func = TruncDate("created_at") - timedelta(days=1)
        else:
            trunc_func = TruncDate("created_at") - timedelta(days=1)

        summary_data = (
            entries.annotate(date=trunc_func)
            .values("date")
            .annotate(entry_count=Count("id"))
            .order_by("date")
        )

        for item in summary_data:
            date = item["date"]
            if period == "week":
                date += timedelta(days=1)  # Adjust for week start
            elif period == "month":
                date = date.replace(day=1)  # Set to first day of month
            item["date"] = date

            # Get category counts for this period
            category_counts = (
                entries.filter(created_at__date=date)
                .values("categories__name")
                .annotate(count=Count("categories"))
            )
            item["category_counts"] = {
                category["categories__name"]: category["count"]
                for category in category_counts
                if category["categories__name"]
            }

        serializer = JournalEntrySerializer(summary_data, many=True)
        return Response(serializer.data)

    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ["categories"]
    search_fields = ["title", "category", "date"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
