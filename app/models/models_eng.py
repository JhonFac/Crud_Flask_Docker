from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKeyConstraint,
    Index,
    Integer,
    PrimaryKeyConstraint,
    SmallInteger,
    String,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class CustomerData(Base):
    __tablename__ = "customer_data"
    type_id = Column(SmallInteger)
    identification = Column(Integer)
    name = Column(String(55))
    phone = Column(String(30))
    email = Column(String(55))
    macro_portfolio = Column(String(20))
    payment_probability = Column(Float)
    customer_segment = Column(String(10))
    customer_type = Column(String(10))
    customer_actions = Column(String(55))
    days_in_arrears = Column(Integer)
    capital_balance = Column(Float)
    income_range = Column(String(20))
    income_trend = Column(String(20))
    sector_indebtedness = Column(Float)
    sector_installments_sum = Column(Float)
    bank_installments_sum = Column(Float)
    entity_1_debt_name = Column(String(20))
    entity_1_debt_value = Column(Float)
    entity_2_debt_name = Column(String(20))
    entity_2_debt_value = Column(Float)
    entity_3_debt_name = Column(String(20))
    entity_3_debt_value = Column(Float)
    minimum_negotiation_payment = Column(Float)
    reference_minimum_installment = Column(Float)
    capital_sum = Column(Float)
    current_interest_sum = Column(Float)
    overdue_interest_sum = Column(Float)
    insurance_sum = Column(Float)
    other_charges_sum = Column(Float)
    minimum_payment = Column(Float)
    restrictive_list_codes = Column(Integer)
    legal_process_stage = Column(String(20))
    recovery_agent_code = Column(String(10))
    certified_income = Column(Float)
    number_of_overdue_products = Column(Integer)
    __table_args__ = (
        PrimaryKeyConstraint("type_id", "identification"),
        UniqueConstraint("type_id", "identification", name="uq_type_id_identification"),
    )


class ProductData(Base):
    __tablename__ = "product_data"
    type_id = Column(SmallInteger)
    identification = Column(Integer)
    cut_off_date = Column(Date)
    product_id = Column(String(18))
    product_family = Column(String(10))
    disbursement = Column(Float)
    term = Column(Integer)
    interest_rate = Column(Float)
    installment = Column(Float)
    in_arrears = Column(Boolean)
    days_in_arrears = Column(Integer)
    capital = Column(Float)
    current_interest = Column(Float)
    arrears_interest = Column(Float)
    insurance = Column(Float)
    other_charges = Column(Float)
    accumulated_payments = Column(Float)
    total_balance = Column(Float)
    minimum_payment = Column(Float)
    promissory_note = Column(Boolean)
    payment_date = Column(Date)
    preapproval_code = Column(String(5))
    company = Column(Integer)
    circular_026 = Column(String(10))
    product_in_dollars = Column(Boolean)
    __table_args__ = (
        PrimaryKeyConstraint("type_id", "identification", "product_id", "cut_off_date"),
        UniqueConstraint("type_id", "identification", "cut_off_date", "product_id", name="uq_product_data"),
    )


class PolicyParameters(Base):
    __tablename__ = "policy_parameters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group = Column(String(20))
    subgroup = Column(String(20))
    policy = Column(String(20))
    value = Column(Float)


class CustomerOffers(Base):
    __tablename__ = "customer_offers"
    type_id = Column(SmallInteger, primary_key=True)
    identification = Column(Integer, primary_key=True)
    offer_1_payment = Column(String(300))
    offer_2_payment = Column(String(300))
    offer_3_payment = Column(String(300))
    offer_1_installment = Column(String(300))
    offer_2_installment = Column(String(300))
    offer_3_installment = Column(String(300))


class DailyResults(Base):
    __tablename__ = "daily_results"
    management_code = Column(String(30), primary_key=True)
    user = Column(String(20))
    type_id = Column(SmallInteger)
    identification = Column(Integer)
    date = Column(DateTime)
    email_update = Column(String(20))
    phone_update = Column(String(20))
    customer_payment = Column(Float)
    selected_offer_on_payment = Column(String(300))
    customer_payment_with_offer = Column(Float)
    customer_installment = Column(Float)
    selected_offer_on_installment = Column(String(300))
    customer_installment_with_offer = Column(Float)
    grace_periods = Column(String(20))
    extraordinary_payment_month_1 = Column(Integer)
    value_month_1 = Column(Float)
    extraordinary_payment_month_2 = Column(Integer)
    value_month_2 = Column(Float)
    condonation_flag = Column(Boolean)
    condonation_item = Column(String(50))
    condonation_percentage = Column(Float)
    condonation_value = Column(Float)
    strategy_code = Column(String(20))
    obligation_payment_date = Column(Date)
    negotiation_status_code = Column(Integer)
    offer_status = Column(Integer)
    recovery_agent = Column(String(20))


class HistoricalResults(Base):
    __tablename__ = "historical_results"
    management_code = Column(String(30), primary_key=True)
    user = Column(String(20))
    type_id = Column(SmallInteger)
    identification = Column(Integer)
    date = Column(DateTime)
    email_update = Column(String(20))
    phone_update = Column(String(20))
    customer_payment = Column(Float)
    selected_offer_on_payment = Column(String(300))
    customer_payment_with_offer = Column(Float)
    customer_installment = Column(Float)
    selected_offer_on_installment = Column(String(300))
    customer_installment_with_offer = Column(Float)
    grace_periods = Column(String(20))
    extraordinary_payment_month_1 = Column(Integer)
    value_month_1 = Column(Float)
    extraordinary_payment_month_2 = Column(Integer)
    value_month_2 = Column(Float)
    condonation_flag = Column(Boolean)
    condonation_item = Column(String(50))
    condonation_percentage = Column(Float)
    condonation_value = Column(Float)
    strategy_code = Column(String(20))
    obligation_payment_date = Column(Date)
    negotiation_status_code = Column(Integer)
    offer_status = Column(Integer)
    recovery_agent = Column(String(20))


class DailyProductNegotiation(Base):
    __tablename__ = "daily_product_negotiation"
    management_code = Column(String(30), primary_key=True)
    type_id = Column(SmallInteger, primary_key=True)
    identification = Column(Integer, primary_key=True)
    cutoff_date = Column(Date, primary_key=True)
    product_id = Column(String(18))
    product_family = Column(String(18))
    disbursement = Column(Float)
    term = Column(Integer)
    rate = Column(Float)
    installment = Column(Float)
    in_arrears = Column(Boolean)
    days_in_arrears = Column(Integer)
    principal = Column(Float)
    current_interest_in_arrears = Column(Float)
    interest_in_arrears = Column(Float)
    mora_insurance = Column(Float)
    other_charges = Column(Float)
    accumulated_payments = Column(Float)
    total_balance = Column(Float)
    minimum_payment = Column(Float)
    promissory_note_flag = Column(Boolean)
    payment_date = Column(Date)
    strategy_code = Column(String(20))
    company = Column(Integer)
    product_status = Column(String(20))


class HistoricalProductNegotiation(Base):
    __tablename__ = "historical_product_negotiation"
    management_code = Column(String(30), primary_key=True)
    type_id = Column(SmallInteger, primary_key=True)
    identification = Column(Integer, primary_key=True)
    cutoff_date = Column(Date, primary_key=True)
    product_id = Column(String(18))
    product_family = Column(String(18))
    disbursement = Column(Float)
    term = Column(Integer)
    rate = Column(Float)
    installment = Column(Float)
    in_arrears = Column(Boolean)
    days_in_arrears = Column(Integer)
    principal = Column(Float)
    current_interest_in_arrears = Column(Float)
    interest_in_arrears = Column(Float)
    mora_insurance = Column(Float)
    other_charges = Column(Float)
    accumulated_payments = Column(Float)
    total_balance = Column(Float)
    minimum_payment = Column(Float)
    promissory_note_flag = Column(Boolean)
    payment_date = Column(Date)
    strategy_code = Column(String(20))
    company = Column(Integer)
    product_status = Column(String(20))


class FTP(Base):
    __tablename__ = "ftp"
    id = Column(Integer, primary_key=True, autoincrement=True)
    term_months = Column(Integer)
    term_days = Column(Integer)
    ftp = Column(Float)
    mv_rate = Column(Float)


class AdvisorMonitoring(Base):
    __tablename__ = "advisor_monitoring"
    user = Column(String(20), primary_key=True)
    segment = Column(String(20))
    action = Column(String(20))
    value = Column(String(100))
    date = Column(Date)


class CustomerAlerts(Base):
    __tablename__ = "customer_alerts"
    management_code = Column(String(30), primary_key=True)
    user = Column(String(20))
    type_id = Column(SmallInteger)
    identification = Column(Integer)
    date = Column(DateTime)
    question_category = Column(String(50))
    question_asked = Column(String(300))
    customer_response = Column(String(200))
    response_validation = Column(Boolean)


class AdvisorManagement(Base):
    __tablename__ = "advisor_management"
    management_code = Column(String(30), primary_key=True)
    user = Column(String(20))
    type_id = Column(SmallInteger)
    identification = Column(Integer)
    date = Column(DateTime)
    management_result = Column(String(20))
    comment_type = Column(String(50))
    comment = Column(String(300))
