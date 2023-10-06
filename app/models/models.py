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


class DatosCliente(Base):
    __tablename__ = "datos_cliente"
    tipo_id = Column(SmallInteger)
    identificacion = Column(Integer)
    nombre = Column(String(55))
    telefono = Column(String(30))
    correo = Column(String(55))
    macroportafolio = Column(String(20))
    probabilidad_pago = Column(Float)
    segmento_cliente = Column(String(10))
    tipo_cliente = Column(String(10))
    acciones_sobre_cliente = Column(String(55))
    dias_mora = Column(Integer)
    saldo_capital = Column(Float)
    rango_ingresos = Column(String(20))
    tendencia_ingresos = Column(String(20))
    endeudamiento_sector = Column(Float)
    suma_cuotas_sector = Column(Float)
    suma_cuotas_banco = Column(Float)
    nombre_entidad_1_deuda = Column(String(20))
    valor_entidad_1_deuda = Column(Float)
    nombre_entidad_2_deuda = Column(String(20))
    valor_entidad_2_deuda = Column(Float)
    nombre_entidad_3_deuda = Column(String(20))
    valor_entidad_3_deuda = Column(Float)
    abono_minimo_negociacion = Column(Float)
    cuota_minima_referencia = Column(Float)
    suma_capital = Column(Float)
    suma_intereses_corriente = Column(Float)
    suma_intereses_mora = Column(Float)
    suma_seguros = Column(Float)
    suma_otros_cargos = Column(Float)
    pago_minimo = Column(Float)
    codigos_listas_restrictivas = Column(Integer)
    etapa_procesos_juridicos = Column(String(20))
    cod_recuperador = Column(String(10))
    ingreso_certificado = Column(Float)
    numero_productos_mora = Column(Integer)
    __table_args__ = (
        PrimaryKeyConstraint("tipo_id", "identificacion"),
        UniqueConstraint("tipo_id", "identificacion", name="uq_tipo_id_identificacion"),
    )
