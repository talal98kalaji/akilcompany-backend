from django.db import migrations

def load_data(apps, schema_editor):
    Brand = apps.get_model('brand', 'Brand')
    Category = apps.get_model('category', 'Category')
    tennin, _ = Brand.objects.get_or_create(
        name='Tennin', 
        defaults={'image': 'brand/images/tennin.png'}
    )
    
    eiffel, _ = Brand.objects.get_or_create(
        name='Eiffel', 
        defaults={'image': 'brand/images/eiffel.png'}
    )
    
    snow_land, _ = Brand.objects.get_or_create(
        name='Snow Land', 
        defaults={'image': 'brand/images/snow_land.png'}
    )
    Category.objects.get_or_create(brand=tennin, name='Men')
    Category.objects.get_or_create(brand=tennin, name='Women')
    Category.objects.get_or_create(brand=tennin, name='Kids')
    Category.objects.get_or_create(brand=eiffel, name='Men')
    Category.objects.get_or_create(brand=eiffel, name='Women')
    Category.objects.get_or_create(brand=eiffel, name='Kids')
    Category.objects.get_or_create(brand=snow_land, name='Men')
    Category.objects.get_or_create(brand=snow_land, name='Women')


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]