### QUERYS PARA CREAR TABLAS #### /* Customer Data */
CREATE TABLE IF NOT EXISTS customer_data (type_id INTEGER UNIQUE,
                                                          identification INTEGER PRIMARY KEY,
                                                                                         name VARCHAR(55),
                                                                                              phone VARCHAR(30),
                                                                                                    email VARCHAR(55),
                                                                                                          macro_portfolio VARCHAR(20),
                                                                                                                          payment_probability REAL, customer_segment VARCHAR(10),
                                                                                                                                                                     customer_type VARCHAR(10),
                                                                                                                                                                                   customer_actions VARCHAR(55),
                                                                                                                                                                                                    days_in_arrears INTEGER, capital_balance REAL, income_range VARCHAR(20),
                                                                                                                                                                                                                                                                income_trend VARCHAR(20),
                                                                                                                                                                                                                                                                             sector_indebtedness REAL, sector_installments_sum REAL, bank_installments_sum REAL, entity_1_debt_name VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                    entity_1_debt_value REAL, entity_2_debt_name VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                                                                 entity_2_debt_value REAL, entity_3_debt_name VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              entity_3_debt_value REAL, minimum_negotiation_payment REAL, reference_minimum_installment REAL, capital_sum REAL, current_interest_sum REAL, overdue_interest_sum REAL, insurance_sum REAL, other_charges_sum REAL, minimum_payment REAL, restrictive_list_codes INTEGER, legal_process_stage VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            recovery_agent_code VARCHAR(10),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                certified_income REAL, number_of_overdue_products INTEGER);

/* Product Data */
CREATE TABLE IF NOT EXISTS product_data (type_id SMALLINT, identification INTEGER PRIMARY KEY,
                                                                                          cut_off_date DATE, product_id VARCHAR(18),
                                                                                                                        product_family VARCHAR(10),
                                                                                                                                       disbursement REAL, term INTEGER, interest_rate REAL, installment REAL, in_arrears BOOLEAN, days_in_arrears INTEGER, capital REAL, current_interest REAL, arrears_interest REAL, insurance REAL, other_charges REAL, accumulated_payments REAL, total_balance REAL, minimum_payment REAL, promissory_note BOOLEAN, payment_date DATE, preapproval_code VARCHAR(5),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             company INTEGER, circular_026 VARCHAR(10),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           product_in_dollars BOOLEAN);

/* Policy Parameters */
CREATE TABLE IF NOT EXISTS policy_parameters (id SERIAL PRIMARY KEY,
                                                                "group" VARCHAR(20),
                                                                        subgroup VARCHAR(20),
                                                                                 policy VARCHAR(20),
                                                                                        value REAL);

/* Customer Offers */
CREATE TABLE IF NOT EXISTS customer_offers (type_id INTEGER UNIQUE,
                                                            identification INTEGER PRIMARY KEY,
                                                                                           offer_1_payment VARCHAR(300),
                                                                                                           offer_2_payment VARCHAR(300),
                                                                                                                           offer_3_payment VARCHAR(300),
                                                                                                                                           offer_1_installment VARCHAR(300),
                                                                                                                                                               offer_2_installment VARCHAR(300),
                                                                                                                                                                                   offer_3_installment VARCHAR(300));

/* Daily Results */
CREATE TABLE IF NOT EXISTS daily_results (management_code VARCHAR(30) PRIMARY KEY,
                                                                              "user" VARCHAR(20),
                                                                                     type_id SMALLINT, identification INTEGER, date TIMESTAMP,
                                                                                                                                    email_update VARCHAR(20),
                                                                                                                                                 phone_update VARCHAR(20),
                                                                                                                                                              customer_payment REAL, selected_offer_on_payment VARCHAR(300),
                                                                                                                                                                                                               customer_payment_with_offer REAL, customer_installment REAL, selected_offer_on_installment VARCHAR(300),
                                                                                                                                                                                                                                                                                                          customer_installment_with_offer REAL, grace_periods VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                              extraordinary_payment_month_1 INTEGER, value_month_1 REAL, extraordinary_payment_month_2 INTEGER, value_month_2 REAL, condonation_flag BOOLEAN, condonation_item VARCHAR(50),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               condonation_percentage REAL, condonation_value REAL, strategy_code VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  obligation_payment_date DATE, negotiation_status_code INTEGER, offer_status INTEGER, recovery_agent VARCHAR(20));

/* Historical Results */
CREATE TABLE IF NOT EXISTS historical_results (management_code VARCHAR(30) PRIMARY KEY,
                                                                                   "user" VARCHAR(20),
                                                                                          type_id SMALLINT, identification INTEGER, date TIMESTAMP,
                                                                                                                                         email_update VARCHAR(20),
                                                                                                                                                      phone_update VARCHAR(20),
                                                                                                                                                                   customer_payment REAL, selected_offer_on_payment VARCHAR(300),
                                                                                                                                                                                                                    customer_payment_with_offer REAL, customer_installment REAL, selected_offer_on_installment VARCHAR(300),
                                                                                                                                                                                                                                                                                                               customer_installment_with_offer REAL, grace_periods VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                   extraordinary_payment_month_1 INTEGER, value_month_1 REAL, extraordinary_payment_month_2 INTEGER, value_month_2 REAL, condonation_flag BOOLEAN, condonation_item VARCHAR(50),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    condonation_percentage REAL, condonation_value REAL, strategy_code VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       obligation_payment_date DATE, negotiation_status_code INTEGER, offer_status INTEGER, recovery_agent VARCHAR(20));

/* Daily Product Negotiation */
CREATE TABLE IF NOT EXISTS daily_product_negotiation (management_code VARCHAR(30) PRIMARY KEY,
                                                                                          type_id SMALLINT UNIQUE,
                                                                                                           identification INTEGER UNIQUE,
                                                                                                                                  cutoff_date DATE, product_id VARCHAR(18),
                                                                                                                                                               product_family VARCHAR(18),
                                                                                                                                                                              disbursement REAL, term INTEGER, rate REAL, installment REAL, in_arrears BOOLEAN, days_in_arrears INTEGER, principal REAL, current_interest_in_arrears REAL, interest_in_arrears REAL, mora_insurance REAL, other_charges REAL, accumulated_payments REAL, total_balance REAL, minimum_payment REAL, promissory_note_flag BOOLEAN, payment_date DATE, strategy_code VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  company INTEGER, product_status VARCHAR(20));

/* Historical Product Negotiation */
CREATE TABLE IF NOT EXISTS historical_product_negotiation (management_code VARCHAR(30) PRIMARY KEY,
                                                                                               type_id SMALLINT UNIQUE,
                                                                                                                identification INTEGER UNIQUE,
                                                                                                                                       cutoff_date DATE, product_id VARCHAR(18),
                                                                                                                                                                    product_family VARCHAR(18),
                                                                                                                                                                                   disbursement REAL, term INTEGER, rate REAL, installment REAL, in_arrears BOOLEAN, days_in_arrears INTEGER, principal REAL, current_interest_in_arrears REAL, interest_in_arrears REAL, mora_insurance REAL, other_charges REAL, accumulated_payments REAL, total_balance REAL, minimum_payment REAL, promissory_note_flag BOOLEAN, payment_date DATE, strategy_code VARCHAR(20),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       company INTEGER, product_status VARCHAR(20));

/* FTP Data */
CREATE TABLE IF NOT EXISTS ftp_data (id SERIAL PRIMARY KEY,
                                                       term_months INTEGER, term_days INTEGER, ftp REAL, mv_rate REAL);

/* Advisor Monitoring */
CREATE TABLE IF NOT EXISTS advisor_monitoring ("user" VARCHAR(20) PRIMARY KEY,
                                                                          segment VARCHAR(20),
                                                                                  action VARCHAR(20),
                                                                                         value VARCHAR(100), date DATE);

/* Customer Alerts */
CREATE TABLE IF NOT EXISTS customer_alerts (management_code VARCHAR(30) PRIMARY KEY,
                                                                                "user" VARCHAR(20),
                                                                                       type_id SMALLINT, identification INTEGER, date TIMESTAMP,
                                                                                                                                      question_category VARCHAR(50),
                                                                                                                                                        question_asked VARCHAR(300),
                                                                                                                                                                       customer_response VARCHAR(200),
                                                                                                                                                                                         response_validation BOOLEAN);

/* Advisor Management */
CREATE TABLE IF NOT EXISTS advisor_management (management_code VARCHAR(30) PRIMARY KEY,
                                                                                   "user" VARCHAR(20),
                                                                                          type_id SMALLINT, identification INTEGER, date TIMESTAMP,
                                                                                                                                         management_result VARCHAR(20),
                                                                                                                                                           comment_type VARCHAR(50),
                                                                                                                                                                        comment VARCHAR(300));

##
Delete tables ## /* Eliminar la tabla Daily Results */
DROP TABLE IF EXISTS daily_results;

/* Eliminar la tabla Historical Results */
DROP TABLE IF EXISTS historical_results;

/* Eliminar la tabla Daily Product Negotiation */
DROP TABLE IF EXISTS daily_product_negotiation;

/* Eliminar la tabla Historical Product Negotiation */
DROP TABLE IF EXISTS historical_product_negotiation;

/* Eliminar la tabla FTP Data */
DROP TABLE IF EXISTS ftp_data;

/* Eliminar la tabla Advisor Monitoring */
DROP TABLE IF EXISTS advisor_monitoring;

/* Eliminar la tabla Customer Alerts */
DROP TABLE IF EXISTS customer_alerts;

/* Eliminar la tabla Advisor Management */
DROP TABLE IF EXISTS advisor_management;

/* Eliminar la tabla Customer Data  */
DROP TABLE IF EXISTS customer_data;

/* Eliminar la tabla customer_offers */
DROP TABLE IF EXISTS customer_offers;

/* Eliminar la tabla datos_cliente */
DROP TABLE IF EXISTS datos_cliente;

/* Eliminar la tabla policy_parameters */
DROP TABLE IF EXISTS policy_parameters;

/* Eliminar la tabla product_data */
DROP TABLE IF EXISTS product_data;

/* Eliminar la tabla product_data */
DROP TABLE IF EXISTS product_data;


INSERT INTO customer_data
VALUES (3,
        123456789,
        'Nom',
        '123-456-7890',
        'correo@example.com',
        'Macroportafo',
        0.85,
        'Segme',
        'T',
        'Acciones Aleatorias',
        30,
        10000.50,
        'Ra',
        'Tendencia Aleatoria',
        0.75,
        500.25,
        300.75,
        'Entidad 1 Aleatoria',
        150.50,
        'Entidad 2 Aleatoria',
        75.25,
        'Entidad 3 Aleatoria',
        30.50,
        50.75,
        25.25,
        1000.75,
        500.50,
        300.25,
        150.50,
        75.25,
        30,
        5,
        'Recupera',
        5500.75,
        5,
        5);


INSERT INTO product_data
VALUES (2,
        123456789,
        '2023-10-10',
        'Product123',
        'FamilyABC',
        5000.0,
        12,
        0.05,
        450.0,
        TRUE,
        15,
        4000.0,
        50.0,
        10.0,
        25.0,
        30.0,
        5000.0,
        100.0,
        200.0,
        TRUE,
        '2023-11-01',
        'asdf',
        1,
        'asdfas',
        TRUE);

