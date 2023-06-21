from django.db import models

# Create your models here.

from django.db import models


sexo =     [('M', 'Masculino'), 
            ('F', 'Feminino')]

class aluno(models.Model):
    matricula_id=models.IntegerField(primary_key=True)
    nomea=models.CharField(max_length=30)
    sexoa= models.CharField(max_length=1, choices=sexo)
    curso=models.CharField(max_length=30)
    cpf=models.CharField(max_length=11)
    endereco=models.CharField(max_length=60)
    celular=models.CharField(max_length=11)


    def __str__(self) -> str:
        return self.nomea
    class Meta:
        managed=False
        db_table='aluno'
        verbose_name='Aluno'
class professor(models.Model):
    masp_id= models.IntegerField(primary_key=True, null=False)
    nomep= models.CharField(max_length=30, null=False)
    dep = models.CharField(max_length=3)
    sexop= models.CharField(max_length=1, choices=sexo)
    
    def __str__(self) -> str:
        return self.nomep
    class Meta:
        managed=False
        db_table='professor'
        verbose_name='Professore'

class disciplina(models.Model):
    
    cod_disc_id=models.IntegerField(primary_key=True, null=False)
    masp_id=models.ForeignKey(professor, db_column='masp_id',null=False, on_delete=models.CASCADE)
    cargahp=models.IntegerField
    cargaht=models.IntegerField
    nomed=models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.nomed
    class Meta:
        managed=False
        db_table='disciplina'
        verbose_name='Disciplina'

class orienta(models.Model):
    masp_id = models.ForeignKey(professor,db_column='masp_id', null=False, on_delete=models.CASCADE)
    matricula_id = models.ForeignKey(aluno,db_column='matricula_id',null=False, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return f'{self.masp_id} || {self.matricula_id}'
    class Meta:
        managed=False
        db_table='orienta'
        verbose_name='Orientaçõe'
    
class cursar(models.Model):
    cod_disc_id = models.ForeignKey(disciplina,db_column='cod_disc_id' ,on_delete=models.CASCADE, null=False)
    matricula_id = models.ForeignKey(aluno, db_column='matricula_id', on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return f'{self.cod_disc_id} || {self.matricula_id}'
    class Meta:
        managed=False
        db_table='cursar'
        verbose_name='Matriculas em Disciplina'