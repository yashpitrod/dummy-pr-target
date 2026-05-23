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
    
    def track_events(self, items: List[Dict]) -> List[bool]:
        """
        Track events - FILE I/O INSIDE LOOP - terrible performance.
        
        Args:
            items: List of items to process
            
        Returns:
            List of tracking results
        """
        results = []
        
        # PERFORMANCE HORROR: Reading file for each item!
        for item in items:
            try:
                # Read file inside loop - N file operations!
                with open("data.txt") as f:
                    data = f.read()
                
                logger.info(f"Event tracked: {item}")
                results.append(True)
            except Exception as e:
                logger.error(f"Event tracking error: {str(e)}")
                results.append(False)
        
        return results
