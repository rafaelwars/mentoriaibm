from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/clientes/", response_model=_schemas.Cliente)
async def create_cliente(
    cliente: _schemas.CreateCliente,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_cliente(cliente=cliente, db=db)


@app.get("/api/clientes/", response_model=List[_schemas.Cliente])
async def get_clientes(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_clientes(db=db)


@app.get("/api/clientes/{cliente_id}/", response_model=_schemas.Cliente)
async def get_cliente(
    cliente_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    cliente = await _services.get_client(db=db, cliente_id=cliente_id)
    if cliente is None:
        raise _fastapi.HTTPException(status_code=404, detail="Cliente does not exist")

    return cliente


@app.delete("/api/clientes/{cliente_id}/")
async def delete_cliente(
    cliente_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    cliente = await _services.get_client(db=db, cliente_id=cliente_id)
    if cliente is None:
        raise _fastapi.HTTPException(status_code=404, detail="Cliente does not exist")

    await _services.delete_cliente(cliente, db=db)

    return "successfully deleted the user"


@app.put("/api/clientes/{cliente_id}/", response_model=_schemas.Cliente)
async def update_cliente(
    cliente_id: int,
    cliente_data: _schemas.CreateCliente,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    cliente = await _services.get_cliente(db=db, cliente_id=cliente_id)
    if cliente is None:
        raise _fastapi.HTTPException(status_code=404, detail="Cliente does not exist")

    return await _services.update_cliente(
        client_data=cliente_data, cliente=cliente, db=db
    )