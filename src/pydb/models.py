'''Lab data models using SQLModel.'''

from datetime import date as date_type
from sqlmodel import Field, Relationship, SQLModel, Session, create_engine, select


class ModelWithDate(SQLModel):
    '''Provide uniform date formatting.'''
    class Config:
        json_encoders = {
            date_type: lambda dt: dt.isoformat() if dt is not None else ''
        }


class Staff(ModelWithDate, table=True):
    '''Lab staff.'''
    staff_id: int = Field(primary_key=True)
    personal: str
    family: str

    performed: list['Performed'] = Relationship(back_populates='staff')


class Experiment(ModelWithDate, table=True):
    '''Experiments.'''
    sample_id: int = Field(primary_key=True)
    kind: str
    start: date_type
    end: date_type | None

    performed: list['Performed'] = Relationship(back_populates='experiment')


class Performed(ModelWithDate, table=True):
    '''Who did what experiments?'''
    staff_id: int = Field(foreign_key='staff.staff_id')
    sample_id: int = Field(foreign_key='experiment.sample_id')

    rowid: int = Field(primary_key=True)
    staff: Staff = Relationship(back_populates='performed')
    experiment: Experiment = Relationship(back_populates='performed')


if __name__ == '__main__':
    TABLES = [
        Staff,
        Experiment,
        Performed,
    ]
    import sys
    dbfile = sys.argv[1]
    engine = create_engine(f'sqlite:///{dbfile}')
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        for table in TABLES:
            print(table.__name__, len(session.exec(select(table)).all()))
