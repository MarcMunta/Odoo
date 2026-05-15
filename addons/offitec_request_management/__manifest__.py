{
    "name": "OffiTec Request Management",
    "summary": "Manage office furniture requests for OffiTec.",
    "version": "19.0.1.0.0",
    "category": "Operations",
    "author": "Izit",
    "license": "LGPL-3",
    "depends": ["base", "base_import_module"],
    "data": [
        "models/offitec_request_model.xml",
        "security/ir.model.access.csv",
        "views/offitec_request_views.xml",
        "data/offitec_request_data.xml",
    ],
    "installable": True,
    "application": True,
}
