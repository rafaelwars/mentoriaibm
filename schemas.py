import datetime as _dt
import pydantic as _pydantic


class _BaseCliente(_pydantic.BaseModel):
       segmentation_month: int
       ifood_status_last_month: str
       ifood_status: str
       orders_last_91d: int
       qtt_orders_last_year: int
       qtt_valid_orders: int
       last_valid_order_date: int
       qtt_invalid_orders: int
       marlin_tag: str
       recency_months: int
       last_nps: str
       customer_lifetime_days: int
       customer_lifetime_months: int
       was_mub_last_month: str
       buyer_last_91d: str
       recency_days: int
       freq_last_91d: int
       benefits_sensitivity: str
       preferred_shift_bucket: int
       merchant_variety: str
       cod_last_nps: str
       cod_ifood_status_last_month: str
       cod_ifood_status: str
       cod_marlin_tag: str



class Cliente(_BaseCliente):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreateCliente(_BaseCliente):
    pass