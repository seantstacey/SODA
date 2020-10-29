
declare
   dguide clob ;
begin
   select json_dataguide(json_document, DBMS_JSON.FORMAT_HIERARCHICAL)
   into dguide from sodacollection  ;

   dbms_json.create_view('auto_view', 'sodacollection', 'json_document', dguide );
end ;
/


desc auto_view ;

select "name", "infraclass", "family", "venomous"
from   auto_view
order  by 1,2
/
