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


# Atributo: id_type, Valor: 1
# Atributo: identification, Valor: 12345678
# Atributo: name, Valor: Nom
# Atributo: phone, Valor: 123-456-7890
# Atributo: email, Valor: correo@example.com
# Atributo: macro_portfolio, Valor: Macroportafo
# Atributo: payment_probability, Valor: 0.85
# Atributo: customer_segment, Valor: Segme
# Atributo: customer_type, Valor: T
# Atributo: customer_actions, Valor: Acciones Aleatorias
# Atributo: days_in_arrears, Valor: 30
# Atributo: capital_balance, Valor: 10000.5
# Atributo: income_range, Valor: Ra
# Atributo: income_trend, Valor: Tendencia Aleatoria
# Atributo: sector_indebtedness, Valor: 0.75
# Atributo: sector_installments_sum, Valor: 500.25
# Atributo: bank_installments_sum, Valor: 300.75
# Atributo: entity_1_debt_name, Valor: Entidad 1 Aleatoria
# Atributo: entity_1_debt_value, Valor: 150.5
# Atributo: entity_2_debt_name, Valor: Entidad 2 Aleatoria
# Atributo: entity_2_debt_value, Valor: 75.25
# Atributo: entity_3_debt_name, Valor: Entidad 3 Aleatoria
# Atributo: entity_3_debt_value, Valor: 30.5
# Atributo: minimum_negotiation_payment, Valor: 50.75
# Atributo: reference_minimum_installment, Valor: 25.25
# Atributo: capital_sum, Valor: 1000.75
# Atributo: current_interest_sum, Valor: 500.5
# Atributo: overdue_interest_sum, Valor: 300.25
# Atributo: insurance_sum, Valor: 150.5
# Atributo: other_charges_sum, Valor: 75.25
# Atributo: minimum_payment, Valor: 30.0
# Atributo: restrictive_list_codes, Valor: 5
# Atributo: legal_process_stage, Valor: Recupera
# Atributo: recovery_agent_code, Valor: 5500.75
# Atributo: certified_income, Valor: 5.0
# Atributo: number_of_overdue_products, Valor: 5
