import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class MetricsCalculator:
    """Calculate and track application metrics."""
    
    def calculate_metrics(self, data: List[float]) -> Dict:
        """
        Calculate statistical metrics for data.
        
        Args:
            data: List of numeric values
            
        Returns:
            Dictionary with metrics
        """
        if not data:
            return {"count": 0, "sum": 0, "average": 0}
        
        total = sum(data)
        count = len(data)
        average = total / count
        
        logger.info(f"Calculated metrics for {count} items")
        
        return {
            "count": count,
            "sum": total,
            "average": average,
            "min": min(data),
            "max": max(data)
        }
    
    def track_event(self, event_name: str, event_data: Dict) -> bool:
        """
        Track an application event.
        
        Args:
            event_name: Name of the event
            event_data: Event data
            
        Returns:
            True if tracking successful
        """
        try:
            logger.info(f"Event tracked: {event_name}")
            return True
        except Exception as e:
            logger.error(f"Event tracking error: {str(e)}")
            return False
