db.define_table(
   'events',
   Field('lat', notnull=True),
   Field('lon', notnull=True),
   Field('description')
)
