# 📊 Stock Monetary API

A FastAPI-based REST API that provides financial data about public companies in the USA, with support for versioned endpoints. You can subscribe and support my work through RapidAPI: TODO

## 📚 Sample API Data

`GET` `/api/v1/statements/{ticker_symbol}` `ticker_symbol — O`

```json
{
    "TotalRevenue": {
        "2025-06-30":281724000000.0,
        "2024-06-30":245122000000.0,
        "2023-06-30":211915000000.0,
        "2022-06-30":198270000000.0,
        "2021-06-30":168088000000.0,
        "2020-06-30":143015000000.0,
        "2019-06-30":125843000000.0,
        "2018-06-30":110360000000.0,
        "2017-06-30":96571000000.0,
        "2016-06-30":91154000000.0,
        "2015-06-30":75956000000.0,
        "2014-06-30":72948000000.0,
        "2013-06-30":77849000000.0,
        "2012-06-30":73723000000.0,
        "2011-06-30":69943000000.0,
        "2010-06-30":62484000000.0,
        "2009-06-30":58437000000.0,
        "2008-06-30":60420000000.0
}...
```

## 🛠️ Tech Stack

- ⚡ **FastAPI** – Web framework
- 🔥 **Uvicorn** – ASGI server
- 🐘 **PostgreSQL** – Relational database
- 🧪 **PyTest** – Testing framework
- 📏 **flake8** – Linter for Python code
- 🐳 **Docker** – Containerization
- 🚀 **Heroku** – Deployment platform
