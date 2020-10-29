create user SCOTT identified by <My Password> ;
 
grant DWROLE, UNLIMITED TABLESPACE to SCOTT ; 


-- Grant access to the SQLDeveloperWeb console to our user SCOTT too:

BEGIN
   ORDS.enable_schema(
   p_enabled => TRUE,
   p_schema => 'SCOTT',
   p_url_mapping_type => 'BASE_PATH',
   p_url_mapping_pattern => 'scott',
   p_auto_rest_auth => FALSE ) ;

   COMMIT;
END;
/
