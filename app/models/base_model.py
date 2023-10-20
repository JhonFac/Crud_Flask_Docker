from app.utils.database import get_db


class BaseModel:
    tablename = ""
    schema = "public"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def __product_keys__(cls, cursor):
        cursor.execute(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{cls.schema}' and TABLE_NAME = '{cls.tablename}' order by ORDINAL_POSITION"
        )
        keys = cursor.fetchall()
        keys = [key[0] for key in keys]
        return keys

    @classmethod
    def get_by_id(cls, id_type: int, id_num: int, many: bool = False):
        db = get_db()
        cursor = db.cursor()
        keys = cls.__product_keys__(cursor=cursor)
        cursor.execute(
            f"SELECT * FROM {cls.schema}.{cls.tablename} WHERE type_id = {str(id_type)} AND identification = {str(id_num)}"
        )
        result = cursor.fetchall() if many else cursor.fetchone()
        if result:
            return [cls(**dict(zip(keys, row))) for row in result] if many else cls(**dict(zip(keys, result)))
        return None
