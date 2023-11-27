import datetime as _dt
import sqlalchemy as _sql

import database as _database

class Cliente(_database.Base):
    __tablename__ = "cliente"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    segmentation_month = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    ifood_status_last_month = _sql.Column(_sql.Integer, primary_key=True, index=True)
    ifood_status = _sql.Column(_sql.String, index=True)
    orders_last_91d = _sql.Column(_sql.Integer, primary_key=True, index=True)
    qtt_orders_last_year = _sql.Column(_sql.Integer, primary_key=True, index=True)
    qtt_valid_orders = _sql.Column(_sql.Integer, primary_key=True, index=True)
    last_valid_order_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    qtt_invalid_orders = _sql.Column(_sql.Integer, primary_key=True, index=True)
    marlin_tag = _sql.Column(_sql.String, index=True)
    recency_months = _sql.Column(_sql.Integer, primary_key=True, index=True)
    last_nps = _sql.Column(_sql.String, index=True)
    customer_lifetime_days = _sql.Column(_sql.Integer, primary_key=True, index=True)
    customer_lifetime_months =	_sql.Column(_sql.Integer, primary_key=True, index=True)
    was_mub_last_month = _sql.Column(_sql.String, index=True)
    buyer_last_91d = _sql.Column(_sql.String, index=True)
    recency_days = _sql.Column(_sql.Integer, primary_key=True, index=True)
    freq_last_91d = _sql.Column(_sql.Integer, primary_key=True, index=True)
    benefits_sensitivity = _sql.Column(_sql.String, index=True)
    preferred_shift_bucket = _sql.Column(_sql.Integer, primary_key=True, index=True)
    merchant_variety = _sql.Column(_sql.String, index=True)
    cod_last_nps = _sql.Column(_sql.String, index=True)
    cod_ifood_status_last_month = _sql.Column(_sql.String, index=True)
    cod_ifood_status = _sql.Column(_sql.String, index=True)
    cod_marlin_tag = _sql.Column(_sql.String, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)