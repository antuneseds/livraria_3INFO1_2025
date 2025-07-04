from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_user_is_active_alter_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True, help_text="Indica que este usuário está ativo.", verbose_name="Usuário está ativo"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Indica que este usuário pode acessar o Admin.",
                verbose_name="Usuário é da equipe",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, help_text="Username", max_length=255, null=True, verbose_name="name"),
        ),
    ]