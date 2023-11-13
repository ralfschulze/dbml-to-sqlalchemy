"""Tests for the dbml2sqlalchemy module"""
import dbml2sqlalchemy.dbml2sqlalchemy as dbml2py

def test_match_type():
    """Test conversion from DBML types to SQLAlchemy types"""

    assert "Geometry(geometry_type='POINT', srid=25832)" == dbml2py.match_type(
        "geometry(POINT,25832)"
    )
    assert (
        "Geometry(geometry_type='LINESTRING', srid=25832)"
        == dbml2py.match_type("geometry(LINESTRING,25832)")
    )
    assert "Geometry(geometry_type='POLYGON')" == dbml2py.match_type(
        "geometry(POLYGON)"
    )

    assert "Float" == dbml2py.match_type("float")
    assert "DateTime" == dbml2py.match_type("datetime")
    assert "TIMESTAMP" == dbml2py.match_type("timestamp")
    assert "ARRAY(Float)" == dbml2py.match_type("float[]")
