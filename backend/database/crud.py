from .models import MuskDetection

def create_musk_detection(db, timestamp, total_faces, masked, unmasked, incorrectly_masked, compliance_percentage):
    new_detection = MuskDetection(
        timestamp=timestamp,
        total_faces=total_faces,
        masked=masked,
        unmasked=unmasked,
        incorrectly_masked=incorrectly_masked,
        compliance_percentage=compliance_percentage
    )
    db.add(new_detection)
    db.commit()
    db.refresh(new_detection)
    return new_detection

def get_musk_detections(db, skip: int = 0, limit: int = 100):
    return db.query(MuskDetection).offset(skip).limit(limit).all()