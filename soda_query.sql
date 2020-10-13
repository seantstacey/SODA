desc sodacollection

select * 
from   sodacollection
/

select id,
       created_on,
       last_modified,
       version,
       json_serialize(json_document returning varchar2 pretty) pretty_js
from   sodacollection
/

