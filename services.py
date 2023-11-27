from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_cliente(
    cliente: _schemas.CreateCliente, db: "Session"
) -> _schemas.Cliente:
    cliente = _models.Cliente(**cliente.dict())
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return _schemas.Cliente.from_orm(cliente)


async def get_all_clientes(db: "Session") -> List[_schemas.Cliente]:
    clientes = db.query(_models.Cliente).all()
    return list(map(_schemas.Cliente.from_orm, clientes))


async def get_cliente(cliente_id: int, db: "Session"):
    cliente = db.query(_models.Cliente).filter(_models.Cliente.id == cliente_id).first()
    return cliente


async def delete_cliente(cliente: _models.Cliente, db: "Session"):
    db.delete(cliente)
    db.commit()


async def update_cliente(
    cliente_data: _schemas.CreateCliente, cliente: _models.Cliente, db: "Session"
) ->   _schemas.Cliente:
       segmentation_month = cliente_data.segmentation_month 
       ifood_status_last_month = cliente_data.ifood_status_last_month
       ifood_status = cliente_data.ifood_status
       orders_last_91d = cliente_data.orders_last_91d 
       qtt_orders_last_year = cliente_data.qtt_orders_last_year
       qtt_valid_orders = cliente_data.qtt_valid_orders
       last_valid_order_date = cliente_data.last_valid_order_date
       qtt_invalid_orders = cliente_data.qtt_invalid_orders
       marlin_tag = cliente_data.marlin_tag
       recency_months = cliente_data.recency_months
       last_nps = cliente_data.last_nps
       customer_lifetime_days = cliente_data.customer_lifetime_days
       customer_lifetime_months = cliente_data.customer_lifetime_months
       was_mub_last_month = cliente_data.was_mub_last_month 
       buyer_last_91d = cliente_data.buyer_last_91d 
       recency_days = cliente_data.recency_days
       freq_last_91d = cliente_data.freq_last_91d
       benefits_sensitivity = cliente_data.benefits_sensitivity
       preferred_shift_bucket = cliente_data.preferred_shift_bucket
       merchant_variety = cliente_data.merchant_variety
       cod_last_nps = cliente_data.cod_last_nps
       cod_ifood_status_last_month = cliente_data.cod_ifood_status_last_month
       cod_ifood_status = cliente_data.cod_ifood_status
       cod_marlin_tag = cliente_data.cod_marlin_tag

       db.commit()
       db.refresh(cliente)

       return _schemas.Cliente.from_orm(cliente)