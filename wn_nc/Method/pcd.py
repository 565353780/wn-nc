import numpy as np

def toNormalizedPoints(points_unnormalized: np.ndarray, bbox_scale: float = 1.1) -> np.ndarray:
    bbox_center = (points_unnormalized.min(0) + points_unnormalized.max(0)) / 2.
    bbox_len = (points_unnormalized.max(0) - points_unnormalized.min(0)).max()
    points_normalized = (points_unnormalized - bbox_center) * (2 / (bbox_len * bbox_scale))
    return points_normalized
