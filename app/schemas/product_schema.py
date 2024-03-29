from marshmallow import Schema, fields


class ProductDataSchema(Schema):
    type_id = fields.Int(required=True)
    identification = fields.Int(required=True)
    cut_off_date = fields.Date(required=True)
    product_id = fields.Str(required=True)
    product_family = fields.Str()
    disbursement = fields.Float()
    term = fields.Int()
    interest_rate = fields.Float()
    installment = fields.Float()
    in_arrears = fields.Bool()
    days_in_arrears = fields.Int()
    capital = fields.Float()
    current_interest = fields.Float()
    arrears_interest = fields.Float()
    insurance = fields.Float()
    other_charges = fields.Float()
    accumulated_payments = fields.Float()
    total_balance = fields.Float()
    minimum_payment = fields.Float()
    promissory_note = fields.Bool()
    payment_date = fields.Date()
    preapproval_code = fields.Str()
    company = fields.Int()
    circular_026 = fields.Str()
    product_in_dollars = fields.Bool()
