# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Cen(models.Model):
#     folioc = models.FloatField(blank=True, null=True)
#     p_global = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'CEN'


# class Normal2808RefSito(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col005 = models.CharField(db_column='Col005', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col006 = models.CharField(db_column='Col006', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col007 = models.CharField(db_column='Col007', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col008 = models.CharField(db_column='Col008', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col009 = models.CharField(db_column='Col009', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'NORMAL 2808 REF sito'


# class NormalReferenciasSito2(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col005 = models.CharField(db_column='Col005', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col006 = models.CharField(db_column='Col006', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col007 = models.CharField(db_column='Col007', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col008 = models.CharField(db_column='Col008', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col009 = models.CharField(db_column='Col009', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'NORMAL_REFERENCIAS sito2'


# class Referencia(models.Model):
#     referencia = models.CharField(max_length=30)
#     matricula = models.CharField(max_length=12)
#     fechalimite = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'Referencia'


# class Resultados(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8000)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=8000)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=8000)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=8000)  # Field name made lowercase.
#     col005 = models.CharField(db_column='Col005', max_length=8000)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Resultados'


# class AcademiaIdiomas(models.Model):
#     cve_materia = models.IntegerField()
#     cve_plan_estudio = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'academia_idiomas'


# class ActivPpga(models.Model):
#     cve_activ_ppga = models.IntegerField(primary_key=True)
#     cve_tema_psicopedagogico = models.IntegerField()
#     cve_tipo_actividad_tutoreo_alumno = models.IntegerField()
#     cve_modalidad_tema_ppg = models.IntegerField()
#     cve_coordinador_tutoreo = models.CharField(max_length=10)
#     fecha = models.DateTimeField()
#     observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'activ_ppga'


# class ActivPpgaAlumno(models.Model):
#     cve_activ_ppga = models.IntegerField()
#     matricula = models.CharField(max_length=12)
#     cve_grupo = models.SmallIntegerField()
#     observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'activ_ppga_alumno'


# class ActivPpgaGrupo(models.Model):
#     cve_activ_ppga = models.IntegerField()
#     cve_grupo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'activ_ppga_grupo'


# class ActivPpgt(models.Model):
#     cve_activ_ppgt = models.IntegerField(primary_key=True)
#     cve_tipo_actividad_tutoreo_tutor = models.IntegerField()
#     cve_coordinador_tutoreo = models.CharField(max_length=10)
#     cve_periodo = models.SmallIntegerField()
#     fecha = models.DateTimeField()
#     observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'activ_ppgt'


# class ActivPpgtTutor(models.Model):
#     cve_activ_ppgt = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_grupo = models.SmallIntegerField()
#     observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'activ_ppgt_tutor'


# class Actividad(models.Model):
#     cve_actividad = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'actividad'


# class Administrativo(models.Model):
#     cve_empleado = models.CharField(primary_key=True, max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'administrativo'


# class AgrupacionCotizacion(models.Model):
#     cve_agrupacion = models.IntegerField(primary_key=True)
#     cve_cotizacion = models.IntegerField()
#     cantidad = models.IntegerField()
#     cve_unidad_medida = models.SmallIntegerField()
#     descripcion = models.TextField()  # This field type is a guess.
#     precio_unitario = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'agrupacion_cotizacion'
#         unique_together = (('cve_agrupacion', 'cve_cotizacion'),)


# class AhorroIsseg(models.Model):
#     cve_empleado = models.CharField(primary_key=True, max_length=10)
#     cantidad = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'ahorro_isseg'


# class Alumno(models.Model):
#     cve_alumno = models.IntegerField()
#     matricula = models.CharField(primary_key=True, max_length=12)
#     fecha_ingreso = models.DateTimeField()
#     status = models.CharField(max_length=2)
#     generacion = models.CharField(max_length=6, blank=True, null=True)
#     status_academico = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'alumno'


# class AlumnoActa(models.Model):
#     cve_periodo = models.SmallIntegerField()
#     matricula = models.CharField(primary_key=True, max_length=12)
#     numero_folio = models.CharField(max_length=5)
#     numero_tomo = models.CharField(max_length=5)
#     numero_foja = models.CharField(max_length=5)
#     fecha_entrega = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_acta'
#         unique_together = (('matricula', 'cve_periodo'),)


# class AlumnoActaCancelada(models.Model):
#     numero_folio = models.CharField(max_length=5)
#     cve_periodo = models.IntegerField()
#     matricula = models.CharField(max_length=12)
#     numero_tomo = models.CharField(max_length=5)
#     numero_foja = models.CharField(max_length=5)
#     fecha_entrega = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_acta_cancelada'


# class AlumnoCalificacionCriterio(models.Model):
#     matricula = models.OneToOneField('AlumnoCalificacionParcial', models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_clase = models.ForeignKey('AlumnoCalificacionParcial', models.DO_NOTHING, db_column='cve_clase')
#     cve_docente = models.ForeignKey('AlumnoCalificacionParcial', models.DO_NOTHING, db_column='cve_docente')
#     no_parcial = models.ForeignKey('AlumnoCalificacionParcial', models.DO_NOTHING, db_column='no_parcial')
#     cve_criterio = models.IntegerField()
#     cve_periodo_captura = models.ForeignKey('PeriodoCapturaCalificacion', models.DO_NOTHING, db_column='cve_periodo_captura')
#     calificacion = models.FloatField(blank=True, null=True)
#     fecha_captura = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_calificacion_criterio'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'no_parcial', 'cve_criterio'),)


# class AlumnoCalificacionParcial(models.Model):
#     matricula = models.OneToOneField('AlumnoClase', models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_clase = models.ForeignKey('AlumnoClase', models.DO_NOTHING, db_column='cve_clase')
#     cve_docente = models.ForeignKey('AlumnoClase', models.DO_NOTHING, db_column='cve_docente')
#     no_parcial = models.SmallIntegerField()
#     calificacion = models.FloatField()
#     cve_status_calificacion = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_calificacion_parcial'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'no_parcial'),)


# class AlumnoCalificacionUnidadTematica(models.Model):
#     matricula = models.CharField(max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     no_parcial = models.IntegerField()
#     unidad_tematica = models.IntegerField()
#     cve_periodo_captura = models.IntegerField()
#     calificacion = models.FloatField()
#     faltas_unidad = models.IntegerField()
#     cve_status_calificacion = models.IntegerField()
#     fecha_captura = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_calificacion_unidad_tematica'


# class AlumnoCertificado(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=9)
#     cve_periodo = models.SmallIntegerField()
#     numero_certificado = models.CharField(max_length=5)
#     numero_libro = models.CharField(max_length=5)
#     numero_foja = models.CharField(max_length=5)
#     fecha_entrega = models.DateTimeField()
#     numero_asignatura = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'alumno_certificado'
#         unique_together = (('matricula', 'cve_periodo'),)


# class AlumnoCertificadoCancelado(models.Model):
#     numero_certificado = models.CharField(max_length=5)
#     cve_periodo = models.IntegerField()
#     matricula = models.CharField(max_length=12)
#     numero_libro = models.CharField(max_length=5)
#     numero_foja = models.CharField(max_length=5)
#     fecha_entrega = models.DateTimeField()
#     numero_asignatura = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'alumno_certificado_cancelado'


# class AlumnoCertificadoParcial(models.Model):
#     matricula = models.CharField(max_length=8)
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()
#     folio = models.CharField(max_length=5)
#     libro = models.CharField(max_length=5)
#     foja = models.CharField(max_length=5)
#     fecha_entrega = models.DateTimeField()
#     numero_asignatura = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'alumno_certificado_parcial'


# class AlumnoCertificadoParcialLic(models.Model):
#     matricula = models.CharField(max_length=8)
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()
#     folio = models.CharField(max_length=5)
#     libro = models.CharField(max_length=5)
#     foja = models.CharField(max_length=5)
#     fecha_entrega = models.DateTimeField()
#     numero_asignatura = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'alumno_certificado_parcial_lic'


# class AlumnoClase(models.Model):
#     matricula = models.OneToOneField(Alumno, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_clase = models.ForeignKey('Clase', models.DO_NOTHING, db_column='cve_clase')
#     cve_docente = models.ForeignKey('Clase', models.DO_NOTHING, db_column='cve_docente')
#     cve_status = models.SmallIntegerField(blank=True, null=True)
#     calificacion_final = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_clase'
#         unique_together = (('matricula', 'cve_docente', 'cve_clase'),)


# class AlumnoClaseOptativa(models.Model):
#     cve_optativa = models.IntegerField(primary_key=True)
#     matricula = models.CharField(max_length=12)
#     cve_docente = models.CharField(max_length=10)
#     cve_clase = models.IntegerField()
#     grupo = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'alumno_clase_optativa'
#         unique_together = (('cve_optativa', 'matricula', 'cve_docente', 'cve_clase'),)


# class AlumnoGrupo(models.Model):
#     matricula = models.OneToOneField(Alumno, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='cve_grupo')

#     class Meta:
#         managed = False
#         db_table = 'alumno_grupo'
#         unique_together = (('matricula', 'cve_grupo'),)


# class AlumnoGrupoIdioma(models.Model):
#     cve_grupo_idioma = models.OneToOneField('GrupoIdioma', models.DO_NOTHING, db_column='cve_grupo_idioma', primary_key=True)
#     cve_materia = models.ForeignKey('Materia', models.DO_NOTHING, db_column='cve_materia')
#     matricula_alumno = models.CharField(max_length=15)

#     class Meta:
#         managed = False
#         db_table = 'alumno_grupo_idioma'
#         unique_together = (('cve_grupo_idioma', 'cve_materia', 'matricula_alumno'),)


# class AlumnoGrupoIngles(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_grupo_ingles = models.ForeignKey('GrupoIngles', models.DO_NOTHING, db_column='cve_grupo_ingles')
#     cve_periodo = models.SmallIntegerField()
#     cve_carrera = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_grupo_ingles'
#         unique_together = (('matricula', 'cve_grupo_ingles'),)


# class AlumnoGrupoOptativa(models.Model):
#     matricula = models.CharField(max_length=12)
#     cve_grupo_optativa = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     cve_carrera = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_grupo_optativa'


# class AlumnoPonderacionUnidad(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     no_parcial = models.SmallIntegerField()
#     ponderacion = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_ponderacion_unidad'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'no_parcial'),)


# class AlumnoPonderacionUnidadRemedial(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     no_parcial = models.SmallIntegerField()
#     ponderacion = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_ponderacion_unidad_remedial'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'no_parcial'),)


# class AlumnoReferencia(models.Model):
#     matricula = models.CharField(max_length=12)
#     referencia = models.CharField(max_length=30)
#     fecha = models.DateTimeField()
#     cantidad = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'alumno_referencia'


# class AlumnosEstatusUno(models.Model):
#     cve_alumno = models.IntegerField()
#     matricula = models.CharField(max_length=12)
#     fecha_ingreso = models.DateTimeField()
#     status = models.CharField(max_length=1)
#     generacion = models.CharField(max_length=6, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'alumnos_estatus_uno'


# class ArchivoExcel(models.Model):
#     cve_archivo_excel = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     ruta = models.CharField(max_length=300)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'archivo_excel'


# class Area(models.Model):
#     cve_area = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     centro_costo = models.CharField(max_length=5, blank=True, null=True)
#     abreviatura = models.CharField(max_length=10, blank=True, null=True)
#     cve_unidad_academica = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'area'


# class AreaAcademica(models.Model):
#     cve_area_academica = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()
#     cve_unidad_academica = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'area_academica'


# class AreaConocimiento(models.Model):
#     cve_area_conocimiento = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=40)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'area_conocimiento'


# class AreaEspacio(models.Model):
#     cve_area_espacio = models.IntegerField(primary_key=True)
#     cve_plantel = models.ForeignKey('Plantel', models.DO_NOTHING, db_column='cve_plantel', blank=True, null=True)
#     nombre = models.CharField(max_length=150, blank=True, null=True)
#     nomenclatura = models.CharField(max_length=20, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'area_espacio'


# class Articulo(models.Model):
#     cve_articulo = models.IntegerField(primary_key=True)
#     cve_partida = models.ForeignKey('Partida', models.DO_NOTHING, db_column='cve_partida')
#     nombre = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'articulo'


# class ArticuloAgrupacion(models.Model):
#     cve_articulo_agrupacion = models.IntegerField(primary_key=True)
#     cve_requisicion = models.IntegerField()
#     cve_articulo = models.IntegerField()
#     cve_agrupacion = models.IntegerField()
#     cve_cotizacion = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'articulo_agrupacion'


# class AsignacionEmpleado(models.Model):
#     cve_registro = models.IntegerField()
#     cve_centro_gestor = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'asignacion_empleado'


# class AsignacionResponsable(models.Model):
#     cve_responsable = models.IntegerField()
#     cve_centro_gestor = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'asignacion_responsable'


# class AsistenciaEvento(models.Model):
#     cve_evento = models.IntegerField(primary_key=True)
#     id_persona = models.CharField(max_length=12)
#     activo = models.BooleanField()
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'asistencia_evento'
#         unique_together = (('cve_evento', 'id_persona'),)


# class AsistenciaExamenAdmision(models.Model):
#     folio_ceneval = models.OneToOneField('FichaAdmision', models.DO_NOTHING, db_column='folio_ceneval', primary_key=True)
#     cve_ficha = models.ForeignKey('FichaAdmision', models.DO_NOTHING, db_column='cve_ficha')
#     cve_solicitud_admision = models.ForeignKey('FichaAdmision', models.DO_NOTHING, db_column='cve_solicitud_admision')
#     grupo = models.CharField(max_length=10)
#     asistencia = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'asistencia_examen_admision'
#         unique_together = (('folio_ceneval', 'cve_ficha', 'cve_solicitud_admision'),)


# class Asistente(models.Model):
#     cve_asistente = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'asistente'


# class AsistenteEvento(models.Model):
#     cve_evento = models.IntegerField()
#     cve_asistente = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'asistente_evento'


# class Aspirante(models.Model):
#     cve_aspirante = models.IntegerField(primary_key=True)
#     cve_cuestionario = models.IntegerField()
#     fecha_registro = models.DateTimeField()
#     status = models.CharField(max_length=10)
#     foto = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'aspirante'


# class AspiranteLic(models.Model):
#     cve_aspirante = models.IntegerField(primary_key=True)
#     cve_cuestionario = models.IntegerField()
#     fecha_registro = models.DateTimeField()
#     status = models.CharField(max_length=10)
#     promedio = models.FloatField(blank=True, null=True)
#     aceptado = models.BooleanField(blank=True, null=True)
#     fecha_inscripcion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'aspirante_lic'


# class AspiranteLicProf(models.Model):
#     cve_aspirante = models.IntegerField()
#     cve_cuestionario = models.IntegerField()
#     fecha_registro = models.DateTimeField()
#     status = models.CharField(max_length=10)
#     promedio = models.FloatField(blank=True, null=True)
#     aceptado = models.BooleanField(blank=True, null=True)
#     fecha_inscripcion = models.DateTimeField(blank=True, null=True)
#     cve_solicitud_admision = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'aspirante_lic_prof'


# class AspiranteOtraUniversidad(models.Model):
#     cve_persona = models.IntegerField(primary_key=True)
#     cve_otra_universidad = models.IntegerField(blank=True, null=True)
#     cve_otra_carrera = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'aspirante_otra_universidad'


# class AulaAspirante(models.Model):
#     cve_aula = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     cve_edificio = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'aula_aspirante'


# class AulaIngles(models.Model):
#     cve_aula = models.IntegerField()
#     nombre = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'aula_ingles'


# class AulaSerch(models.Model):
#     cve_aula = models.SmallIntegerField(primary_key=True)
#     cve_edificio = models.ForeignKey('Edificio', models.DO_NOTHING, db_column='cve_edificio', blank=True, null=True)
#     nombre = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'aula_serch'


# class AutorizacionOficio(models.Model):
#     cve_oficio = models.OneToOneField('OficioComision', models.DO_NOTHING, db_column='cve_oficio', primary_key=True)
#     cve_persona = models.IntegerField()
#     cve_tipo_persona = models.IntegerField()
#     fecha_autorizacion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'autorizacion_oficio'
#         unique_together = (('cve_oficio', 'cve_persona'),)


# class AutorizacionOficioCaja(models.Model):
#     cve_autorizacion = models.IntegerField(primary_key=True)
#     cve_oficio = models.ForeignKey('OficioComision', models.DO_NOTHING, db_column='cve_oficio')
#     cve_empleado = models.CharField(max_length=10)
#     fecha_autorizacion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'autorizacion_oficio_caja'


# class AutorizacionValesGasolina(models.Model):
#     cve_oficio = models.OneToOneField('OficioComision', models.DO_NOTHING, db_column='cve_oficio', primary_key=True)
#     cve_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='cve_persona')
#     fecha_autorizacion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'autorizacion_vales_gasolina'


# class Bachillerato(models.Model):
#     cve_bachillerato = models.IntegerField(primary_key=True)
#     cve_sistema_bachillerato = models.IntegerField()
#     cve_colonia = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     direccion = models.CharField(max_length=100)
#     tipo = models.CharField(max_length=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bachillerato'


# class BachilleratoDifusion(models.Model):
#     cve_bachillerato = models.IntegerField()
#     telefono = models.CharField(max_length=20, blank=True, null=True)
#     fax = models.CharField(max_length=50, blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     calle_1 = models.CharField(max_length=250, blank=True, null=True)
#     calle_2 = models.CharField(max_length=250, blank=True, null=True)
#     cve_tipo = models.IntegerField(blank=True, null=True)
#     convenio = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bachillerato_difusion'


# class BachilleratoFaltante(models.Model):
#     nombre = models.CharField(max_length=200)
#     direccion = models.CharField(max_length=150)
#     colonia = models.CharField(max_length=100)
#     ciudad = models.CharField(max_length=100)
#     estado = models.CharField(max_length=100)
#     registrado = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bachillerato_faltante'


# class BachilleratoTipo(models.Model):
#     cve_tipo = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'bachillerato_tipo'


# class Baja(models.Model):
#     cve_baja = models.IntegerField(primary_key=True)
#     matricula = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='matricula')
#     cve_motivo_baja = models.ForeignKey('MotivoBaja', models.DO_NOTHING, db_column='cve_motivo_baja', blank=True, null=True)
#     cve_tipo = models.ForeignKey('MotivoBaja', models.DO_NOTHING, db_column='cve_tipo', blank=True, null=True)
#     fecha = models.DateTimeField()
#     fecha_ses = models.DateTimeField(blank=True, null=True)
#     cve_periodo = models.IntegerField(blank=True, null=True)
#     fecha_alta = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'baja'


# class BajaEmpleado(models.Model):
#     cve_baja = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10)
#     cve_motivo_baja = models.IntegerField()
#     fecha_baja = models.DateTimeField()
#     cve_usuario = models.CharField(max_length=12)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'baja_empleado'


# class BajaFormal(models.Model):
#     cve_baja = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'baja_formal'


# class Bajas(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col005 = models.CharField(db_column='Col005', max_length=8000, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'bajas'


# class Beca(models.Model):
#     cve_beca = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=500)
#     tipo = models.CharField(max_length=1)
#     servicio_becario = models.BooleanField()
#     descripcion = models.CharField(max_length=500, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'beca'


# class BecaCancelada(models.Model):
#     cve_convocatoria = models.OneToOneField('ResultadoBeca', models.DO_NOTHING, db_column='cve_convocatoria', primary_key=True)
#     matricula = models.ForeignKey('ResultadoBeca', models.DO_NOTHING, db_column='matricula')
#     fecha_cancelacion = models.DateTimeField()
#     observaciones = models.CharField(max_length=100)
#     cve_motivo = models.ForeignKey('MotivoCancelacionBeca', models.DO_NOTHING, db_column='cve_motivo')
#     status = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'beca_cancelada'
#         unique_together = (('cve_convocatoria', 'matricula'),)


# class BeneficiarioEmpleado(models.Model):
#     cve_beneficiario = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10)
#     nombre = models.CharField(max_length=50)
#     apellido_paterno = models.CharField(max_length=50)
#     apellido_materno = models.CharField(max_length=50)
#     fecha_nacimiento = models.DateTimeField()
#     cve_parentesco = models.SmallIntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'beneficiario_empleado'


# class Beneficio(models.Model):
#     cve_beneficio = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=500)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'beneficio'


# class BeneficioEmpleado(models.Model):
#     cve_empleado = models.CharField(primary_key=True, max_length=10)
#     poliza_vida = models.BooleanField()
#     poliza_accidente = models.BooleanField()
#     seguro_gasto_medico = models.BooleanField()
#     prestamo_isseg = models.BooleanField()
#     ahorro_isseg = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'beneficio_empleado'


# class BeneficioProyecto(models.Model):
#     cve_beneficio = models.ForeignKey(Beneficio, models.DO_NOTHING, db_column='cve_beneficio')
#     cve_proyecto = models.IntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     cve_periodo = models.SmallIntegerField(blank=True, null=True)
#     observacion = models.CharField(max_length=200, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'beneficio_proyecto'


# class BeneficioProyectoEmpresa(models.Model):
#     cve_proyecto_empresa = models.OneToOneField('ProyectoEstadiaEmpresa', models.DO_NOTHING, db_column='cve_proyecto_empresa', primary_key=True)
#     cve_beneficio = models.ForeignKey(Beneficio, models.DO_NOTHING, db_column='cve_beneficio')
#     observaciones = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'beneficio_proyecto_empresa'
#         unique_together = (('cve_proyecto_empresa', 'cve_beneficio'),)


# class Bitacora(models.Model):
#     cve_bitacora = models.IntegerField()
#     cve_bachillerato = models.IntegerField(blank=True, null=True)
#     cve_periodo = models.IntegerField(blank=True, null=True)
#     folio = models.CharField(max_length=50, blank=True, null=True)
#     fecha_visita = models.DateTimeField(blank=True, null=True)
#     cve_tipo_actividad = models.IntegerField(blank=True, null=True)
#     observaciones = models.CharField(max_length=250, blank=True, null=True)
#     total_personas_atendidas = models.IntegerField(blank=True, null=True)
#     cve_promotor = models.IntegerField(blank=True, null=True)
#     turno = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bitacora'


# class BitacoraGrupo(models.Model):
#     cve_bitacora = models.IntegerField(blank=True, null=True)
#     cve_grupo_atendido = models.IntegerField(blank=True, null=True)
#     cve_actividad = models.IntegerField(blank=True, null=True)
#     cve_docente = models.CharField(max_length=10, blank=True, null=True)
#     nombre_actividad = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bitacora_grupo'


# class Bloqueos(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     status = models.CharField(max_length=50)
#     cve_periodo = models.IntegerField()
#     cve_persona = models.IntegerField()
#     fecha = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'bloqueos'
#         unique_together = (('matricula', 'status', 'cve_periodo'),)


# class CalendarioPago(models.Model):
#     cve_periodo = models.IntegerField()
#     monto = models.FloatField()
#     descuento = models.FloatField()
#     cargos = models.FloatField()
#     fecha_limite_descuento = models.DateTimeField()
#     fecha_limite_normal = models.DateTimeField()
#     fecha_limite_cargos = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'calendario_pago'


# class CalificacionConsulta(models.Model):
#     cve_calificacion = models.IntegerField(primary_key=True)
#     calificacion = models.FloatField()
#     calificacion_integradora = models.CharField(max_length=2)
#     calificacion_simple = models.CharField(max_length=2)
#     activo = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'calificacion_consulta'


# class CalificacionCriterioRemedial(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=50)
#     no_parcial = models.SmallIntegerField()
#     cve_criterio = models.IntegerField()
#     cve_periodo_captura = models.IntegerField(blank=True, null=True)
#     calificacion = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'calificacion_criterio_remedial'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'no_parcial', 'cve_criterio'),)


# class CalificacionEmpresa(models.Model):
#     cve_empresa = models.OneToOneField('Empresa', models.DO_NOTHING, db_column='cve_empresa', primary_key=True)
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo')
#     cve_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='cve_empleado')
#     cve_rubro_calificacion = models.ForeignKey('RubroCalificacionEmpresa', models.DO_NOTHING, db_column='cve_rubro_calificacion', blank=True, null=True)
#     comentario = models.CharField(max_length=500, blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'calificacion_empresa'
#         unique_together = (('cve_empresa', 'cve_periodo', 'cve_empleado'),)


# class CalificacionRecuperacion(models.Model):
#     cve_clase = models.IntegerField(primary_key=True)
#     cve_docente = models.CharField(max_length=10)
#     no_examen = models.SmallIntegerField()
#     matricula = models.CharField(max_length=12)
#     calificacion = models.FloatField()
#     fecha_captura = models.DateTimeField()
#     unidad_tematica = models.IntegerField()
#     cve_periodo_captura = models.IntegerField()
#     cve_status_calificacion = models.IntegerField()
#     evaluador = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'calificacion_recuperacion'
#         unique_together = (('cve_clase', 'cve_docente', 'no_examen', 'matricula', 'unidad_tematica'),)


# class CalificacionRedondeo(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     minimo = models.FloatField()
#     maximo = models.FloatField()
#     calificacion_redondeo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'calificacion_redondeo'


# class CalificacionRemedial(models.Model):
#     cve_clase = models.IntegerField(primary_key=True)
#     cve_docente = models.CharField(max_length=10)
#     no_examen = models.SmallIntegerField()
#     matricula = models.CharField(max_length=12)
#     calificacion = models.FloatField()
#     fecha_captura = models.DateTimeField()
#     no_unidad = models.IntegerField()
#     cve_status = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'calificacion_remedial'
#         unique_together = (('cve_clase', 'cve_docente', 'no_examen', 'matricula', 'no_unidad'),)


# class CalificacionTablaRecuperacion(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     minimo = models.FloatField()
#     maximo = models.FloatField()
#     calificacion_recuperacion = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'calificacion_tabla_recuperacion'


# class CambioCalificacion(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_solicitud = models.IntegerField()
#     cve_director = models.CharField(max_length=10)
#     no_unidad = models.IntegerField()
#     cve_criterio = models.IntegerField()
#     calificacion_anterior = models.FloatField(blank=True, null=True)
#     calificacion_actual = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cambio_calificacion'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_solicitud', 'cve_director', 'no_unidad', 'cve_criterio'),)


# class CambioCalificacionRecuperacion(models.Model):
#     matricula = models.ForeignKey('SolicitudCambioCalificacionRecuperacion', models.DO_NOTHING, db_column='matricula')
#     cve_clase = models.ForeignKey('SolicitudCambioCalificacionRecuperacion', models.DO_NOTHING, db_column='cve_clase')
#     cve_docente = models.ForeignKey('SolicitudCambioCalificacionRecuperacion', models.DO_NOTHING, db_column='cve_docente')
#     cve_solicitud = models.ForeignKey('SolicitudCambioCalificacionRecuperacion', models.DO_NOTHING, db_column='cve_solicitud')
#     cve_empleado = models.CharField(max_length=10)
#     calificacion_anterior_ponderacion = models.FloatField(blank=True, null=True)
#     calificacion_anterior_real = models.FloatField()
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'cambio_calificacion_recuperacion'


# class CambioCalificacionRemedial(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_solicitud = models.IntegerField()
#     cve_director = models.CharField(max_length=10)
#     no_unidad = models.IntegerField()
#     cve_criterio = models.IntegerField()
#     calificacion_anterior = models.FloatField(blank=True, null=True)
#     calificacion_actual = models.FloatField()
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'cambio_calificacion_remedial'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_solicitud', 'no_unidad', 'cve_criterio'),)


# class CambioHorario(models.Model):
#     cve_solicitud = models.OneToOneField('SolicitudPermiso', models.DO_NOTHING, db_column='cve_solicitud', primary_key=True)
#     cve_empleado = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='cve_empleado')
#     folio = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='folio')
#     fecha_inicio = models.DateTimeField(blank=True, null=True)
#     fecha_fin = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cambio_horario'
#         unique_together = (('cve_solicitud', 'cve_empleado', 'folio'),)


# class CambioPonderacionRegularizacion(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=50)
#     cve_solicitud = models.IntegerField()
#     cve_director = models.CharField(max_length=50)
#     no_unidad = models.IntegerField()
#     calificacion_anterior = models.FloatField()
#     calificacion_actual = models.FloatField()
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'cambio_ponderacion_regularizacion'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_solicitud', 'cve_director', 'no_unidad'),)


# class CambioPonderacionUnidad(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_solicitud = models.IntegerField()
#     cve_director = models.CharField(max_length=10)
#     no_unidad = models.SmallIntegerField()
#     ponderacion_anterior = models.FloatField(blank=True, null=True)
#     ponderacion_actual = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cambio_ponderacion_unidad'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_solicitud', 'cve_director', 'no_unidad'),)


# class CambioPrecioArticulo(models.Model):
#     cve_cambio_precio = models.IntegerField(primary_key=True)
#     cve_agrupacion = models.IntegerField()
#     cve_cotizacion = models.IntegerField()
#     precio_unitario_anterior = models.FloatField(blank=True, null=True)
#     precio_unitario_actual = models.FloatField(blank=True, null=True)
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'cambio_precio_articulo'
#         unique_together = (('cve_cambio_precio', 'cve_agrupacion', 'cve_cotizacion'),)


# class Canalizacion(models.Model):
#     cve_canalizacion = models.IntegerField()
#     cve_catalogo_canalizacion = models.IntegerField(blank=True, null=True)
#     cve_tutor = models.CharField(max_length=10, blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)
#     hora = models.CharField(max_length=5, blank=True, null=True)
#     motivo = models.CharField(max_length=100, blank=True, null=True)
#     observaciones = models.CharField(max_length=1000, blank=True, null=True)
#     respuesta = models.BooleanField(blank=True, null=True)
#     fecha_real = models.DateTimeField(blank=True, null=True)
#     revisado = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'canalizacion'


# class CancelacionOficio(models.Model):
#     cve_cancelacion = models.IntegerField()
#     cve_oficio = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     motivo = models.CharField(max_length=500)
#     fecha_registro = models.DateTimeField()
#     cve_tipo_persona = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'cancelacion_oficio'


# class Capitulo(models.Model):
#     cve_capitulo = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=900)
#     activo = models.BooleanField()
#     clave = models.CharField(max_length=4)
#     cve_naturaleza = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'capitulo'


# class CapturaNomiplus(models.Model):
#     cve_solicitud = models.OneToOneField('SolicitudPermiso', models.DO_NOTHING, db_column='cve_solicitud', primary_key=True)
#     cve_empleado = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='cve_empleado')
#     folio = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='folio')
#     fecha_exportacion = models.DateTimeField(blank=True, null=True)
#     fecha_validacion = models.DateTimeField(blank=True, null=True)
#     exportada = models.BooleanField(blank=True, null=True)
#     validada = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'captura_nomiplus'
#         unique_together = (('cve_solicitud', 'cve_empleado', 'folio'),)


# class CapturaTardia(models.Model):
#     cve_captura = models.IntegerField(primary_key=True)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_motivo = models.SmallIntegerField()
#     no_parcial = models.SmallIntegerField()
#     fecha_captura = models.DateTimeField()
#     observacion = models.CharField(max_length=500)
#     cve_grupo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'captura_tardia'


# class CargoReferencias(models.Model):
#     cve_periodo = models.SmallIntegerField()
#     matricula = models.CharField(max_length=12)
#     cantidad = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'cargo_referencias'


# class Carrera(models.Model):
#     cve_carrera = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     abreviatura = models.CharField(max_length=3, blank=True, null=True)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'carrera'


# class CarreraProyectoEmpresa(models.Model):
#     cve_proyecto_empresa = models.OneToOneField('ProyectoEstadiaEmpresa', models.DO_NOTHING, db_column='cve_proyecto_empresa', primary_key=True)
#     cve_unidad_academica = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'carrera_proyecto_empresa'
#         unique_together = (('cve_proyecto_empresa', 'cve_unidad_academica', 'cve_carrera', 'cve_especialidad'),)


# class CarreraUnidadAcademica(models.Model):
#     cve_area_academica = models.OneToOneField(AreaAcademica, models.DO_NOTHING, db_column='cve_area_academica', primary_key=True)
#     cve_carrera = models.SmallIntegerField()
#     cve_unidad_academica = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'carrera_unidad_academica'
#         unique_together = (('cve_area_academica', 'cve_carrera', 'cve_unidad_academica'),)


# class CarrerasEstadiaEmpresa(models.Model):
#     cve_unidad_carrera = models.IntegerField(primary_key=True)
#     cve_carrera = models.ForeignKey('EspecialidadCarrera', models.DO_NOTHING, db_column='cve_carrera')
#     cve_especialidad = models.ForeignKey('EspecialidadCarrera', models.DO_NOTHING, db_column='cve_especialidad')
#     visible = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'carreras_estadia_empresa'
#         unique_together = (('cve_unidad_carrera', 'cve_carrera', 'cve_especialidad'),)


# class CatalogoCanalizacion(models.Model):
#     cve_catalogo_canalizacion = models.IntegerField()
#     nombre = models.CharField(max_length=80, blank=True, null=True)
#     externa = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'catalogo_canalizacion'


# class CatalogoHorario(models.Model):
#     cve_dia = models.OneToOneField('Dia', models.DO_NOTHING, db_column='cve_dia', primary_key=True)
#     cve_catalogo_horario = models.IntegerField()
#     hora_entrada = models.CharField(max_length=6, blank=True, null=True)
#     hora_salida = models.CharField(max_length=6, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'catalogo_horario'
#         unique_together = (('cve_dia', 'cve_catalogo_horario'),)


# class CatalogoMotivoPsicopedagogico(models.Model):
#     cve_catalogo_motivo_psicopedagogico = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'catalogo_motivo_psicopedagogico'


# class CausaBaja(models.Model):
#     cve_causa = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'causa_baja'


# class Ceneval(models.Model):
#     folio_ceneval = models.CharField(db_column='Folio_ceneval', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     folio = models.FloatField(db_column='FOLIO')  # Field name made lowercase.
#     fecha_apli = models.DateTimeField(db_column='FECHA_APLI', blank=True, null=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sexo = models.CharField(db_column='SEXO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_cine = models.CharField(db_column='ACT_CINE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_depo = models.CharField(db_column='ACT_DEPO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_even = models.CharField(db_column='ACT_EVEN', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_muse = models.CharField(db_column='ACT_MUSE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_orga = models.CharField(db_column='ACT_ORGA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     apli = models.CharField(db_column='APLI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     apoy_eco = models.CharField(db_column='APOY_ECO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     apun_cla = models.CharField(db_column='APUN_CLA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cn = models.FloatField(db_column='CN', blank=True, null=True)  # Field name made lowercase.
#     cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
#     cuan_libr = models.CharField(db_column='CUAN_LIBR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cve_inst = models.CharField(db_column='CVE_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cve_proc = models.CharField(db_column='CVE_PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     edad = models.CharField(db_column='EDAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     edo_bac = models.CharField(db_column='EDO_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esco_mad = models.CharField(db_column='ESCO_MAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esco_pad = models.CharField(db_column='ESCO_PAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esp = models.FloatField(db_column='ESP', blank=True, null=True)  # Field name made lowercase.
#     est_alca = models.CharField(db_column='EST_ALCA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     est_apun = models.CharField(db_column='EST_APUN', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     est_text = models.CharField(db_column='EST_TEXT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     exa_bac = models.CharField(db_column='EXA_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     global_field = models.FloatField(db_column='GLOBAL', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
#     hora_est = models.CharField(db_column='HORA_EST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hrs_trab = models.CharField(db_column='HRS_TRAB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     identifica = models.CharField(db_column='IDENTIFICA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ing_esc = models.CharField(db_column='ING_ESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ing_hab = models.CharField(db_column='ING_HAB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ing_lee = models.CharField(db_column='ING_LEE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ing_oir = models.CharField(db_column='ING_OIR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ingr_fam = models.CharField(db_column='INGR_FAM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     lee_tex = models.CharField(db_column='LEE_TEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     len_ind = models.CharField(db_column='LEN_IND', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     m1 = models.FloatField(db_column='M1', blank=True, null=True)  # Field name made lowercase.
#     m10 = models.FloatField(db_column='M10', blank=True, null=True)  # Field name made lowercase.
#     m11 = models.FloatField(db_column='M11', blank=True, null=True)  # Field name made lowercase.
#     m12 = models.FloatField(db_column='M12', blank=True, null=True)  # Field name made lowercase.
#     m2 = models.FloatField(db_column='M2', blank=True, null=True)  # Field name made lowercase.
#     m3 = models.FloatField(db_column='M3', blank=True, null=True)  # Field name made lowercase.
#     m4 = models.FloatField(db_column='M4', blank=True, null=True)  # Field name made lowercase.
#     m5 = models.FloatField(db_column='M5', blank=True, null=True)  # Field name made lowercase.
#     m6 = models.FloatField(db_column='M6', blank=True, null=True)  # Field name made lowercase.
#     m7 = models.FloatField(db_column='M7', blank=True, null=True)  # Field name made lowercase.
#     m8 = models.FloatField(db_column='M8', blank=True, null=True)  # Field name made lowercase.
#     m9 = models.FloatField(db_column='M9', blank=True, null=True)  # Field name made lowercase.
#     mat = models.FloatField(db_column='MAT', blank=True, null=True)  # Field name made lowercase.
#     mc = models.FloatField(db_column='MC', blank=True, null=True)  # Field name made lowercase.
#     moda_bac = models.CharField(db_column='MODA_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     num_pers = models.CharField(db_column='NUM_PERS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     numero = models.FloatField(db_column='NUMERO', blank=True, null=True)  # Field name made lowercase.
#     oca_exa = models.CharField(db_column='OCA_EXA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     p_cn = models.FloatField(db_column='P_CN', blank=True, null=True)  # Field name made lowercase.
#     p_cs = models.FloatField(db_column='P_CS', blank=True, null=True)  # Field name made lowercase.
#     p_esp = models.FloatField(db_column='P_ESP', blank=True, null=True)  # Field name made lowercase.
#     p_global = models.FloatField(db_column='P_GLOBAL', blank=True, null=True)  # Field name made lowercase.
#     p_m1 = models.FloatField(db_column='P_M1', blank=True, null=True)  # Field name made lowercase.
#     p_m10 = models.FloatField(db_column='P_M10', blank=True, null=True)  # Field name made lowercase.
#     p_m11 = models.FloatField(db_column='P_M11', blank=True, null=True)  # Field name made lowercase.
#     p_m12 = models.FloatField(db_column='P_M12', blank=True, null=True)  # Field name made lowercase.
#     p_m2 = models.FloatField(db_column='P_M2', blank=True, null=True)  # Field name made lowercase.
#     p_m3 = models.FloatField(db_column='P_M3', blank=True, null=True)  # Field name made lowercase.
#     p_m4 = models.FloatField(db_column='P_M4', blank=True, null=True)  # Field name made lowercase.
#     p_m5 = models.FloatField(db_column='P_M5', blank=True, null=True)  # Field name made lowercase.
#     p_m6 = models.FloatField(db_column='P_M6', blank=True, null=True)  # Field name made lowercase.
#     p_m7 = models.FloatField(db_column='P_M7', blank=True, null=True)  # Field name made lowercase.
#     p_m8 = models.FloatField(db_column='P_M8', blank=True, null=True)  # Field name made lowercase.
#     p_m9 = models.FloatField(db_column='P_M9', blank=True, null=True)  # Field name made lowercase.
#     p_mat = models.FloatField(db_column='P_MAT', blank=True, null=True)  # Field name made lowercase.
#     p_mc = models.FloatField(db_column='P_MC', blank=True, null=True)  # Field name made lowercase.
#     p_rm = models.FloatField(db_column='P_RM', blank=True, null=True)  # Field name made lowercase.
#     p_rv = models.FloatField(db_column='P_RV', blank=True, null=True)  # Field name made lowercase.
#     percentil = models.FloatField(db_column='PERCENTIL', blank=True, null=True)  # Field name made lowercase.
#     porcne = models.FloatField(db_column='PORCNE', blank=True, null=True)  # Field name made lowercase.
#     pre_exa1 = models.CharField(db_column='PRE_EXA1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     prom_bac = models.FloatField(db_column='PROM_BAC', blank=True, null=True)  # Field name made lowercase.
#     reg_proc = models.CharField(db_column='REG_PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     rm = models.FloatField(db_column='RM', blank=True, null=True)  # Field name made lowercase.
#     rv = models.FloatField(db_column='RV', blank=True, null=True)  # Field name made lowercase.
#     ser_agua = models.CharField(db_column='SER_AGUA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_alum = models.CharField(db_column='SER_ALUM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_auto = models.CharField(db_column='SER_AUTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_basu = models.CharField(db_column='SER_BASU', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_cabl = models.CharField(db_column='SER_CABL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_calc = models.CharField(db_column='SER_CALC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_cale = models.CharField(db_column='SER_CALE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_cuar = models.CharField(db_column='SER_CUAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_dren = models.CharField(db_column='SER_DREN', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_dvd = models.CharField(db_column='SER_DVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_inte = models.CharField(db_column='SER_INTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_luga = models.CharField(db_column='SER_LUGA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_mic = models.CharField(db_column='SER_MIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_pavi = models.CharField(db_column='SER_PAVI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_pc = models.CharField(db_column='SER_PC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_telc = models.CharField(db_column='SER_TELC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_tele = models.CharField(db_column='SER_TELE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_tv = models.CharField(db_column='SER_TV', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_vide = models.CharField(db_column='SER_VIDE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sit_labma = models.CharField(db_column='SIT_LABMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sit_labpa = models.CharField(db_column='SIT_LABPA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tiem_lee = models.CharField(db_column='TIEM_LEE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tipo_bac = models.CharField(db_column='TIPO_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tipo_exa = models.CharField(db_column='TIPO_EXA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tipo_reg = models.CharField(db_column='TIPO_REG', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     trab_act = models.CharField(db_column='TRAB_ACT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uti_enc = models.CharField(db_column='UTI_ENC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uti_pc = models.CharField(db_column='UTI_PC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     vive_con = models.CharField(db_column='VIVE_CON', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ceneval'


# class Cenevalsiaa(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col005 = models.CharField(db_column='Col005', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col006 = models.IntegerField(db_column='Col006', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'cenevalSIAA'


# class Ceneval08(models.Model):
#     folio = models.CharField(db_column='FOLIO', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     folio2 = models.IntegerField(db_column='FOLIO2', blank=True, null=True)  # Field name made lowercase.
#     sexo = models.CharField(db_column='SEXO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tipo_exa = models.CharField(db_column='TIPO_EXA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tipo_reg = models.CharField(db_column='TIPO_REG', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tipo_resp = models.CharField(db_column='TIPO_RESP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     apli = models.CharField(db_column='APLI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fecha_apli = models.DateTimeField(db_column='FECHA_APLI', blank=True, null=True)  # Field name made lowercase.
#     cve_inst = models.CharField(db_column='CVE_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     identifica = models.CharField(db_column='IDENTIFICA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     folio_ref = models.CharField(db_column='FOLIO_ref', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='NOMBRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     d_fech = models.CharField(db_column='D_FECH', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     m_fech = models.CharField(db_column='M_FECH', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     a_fech = models.CharField(db_column='A_FECH', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     lug_nac = models.CharField(db_column='LUG_NAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     len_ind = models.CharField(db_column='LEN_IND', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     len_ma = models.CharField(db_column='LEN_MA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     len_pa = models.CharField(db_column='LEN_PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     edo_proc = models.CharField(db_column='EDO_PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ciu_bac = models.CharField(db_column='CIU_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nom_bac = models.CharField(db_column='NOM_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cve_proc = models.CharField(db_column='CVE_PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     reg_proc = models.CharField(db_column='REG_PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mod_bac = models.CharField(db_column='MOD_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mod_cicl = models.CharField(db_column='MOD_CICL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     prom_gen = models.CharField(db_column='PROM_GEN', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     me_lyr = models.CharField(db_column='ME_LYR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     me_lmi = models.CharField(db_column='ME_LMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     me_liu = models.CharField(db_column='ME_LIU', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     me_coe = models.CharField(db_column='ME_COE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     me_ind = models.CharField(db_column='ME_IND', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     me_lesp = models.CharField(db_column='ME_LESP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     prom_esp = models.CharField(db_column='PROM_ESP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mm_al = models.CharField(db_column='MM_AL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mm_ge = models.CharField(db_column='MM_GE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mm_tri = models.CharField(db_column='MM_TRI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mm_ga = models.CharField(db_column='MM_GA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mm_cdi = models.CharField(db_column='MM_CDI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mm_prob = models.CharField(db_column='MM_PROB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mm_est = models.CharField(db_column='MM_EST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     prom_mat = models.CharField(db_column='PROM_MAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     exa_extr = models.CharField(db_column='EXA_EXTR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mat_rep = models.CharField(db_column='MAT_REP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     beca = models.CharField(db_column='BECA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_fal = models.CharField(db_column='CON_FAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_tar = models.CharField(db_column='CON_TAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_ent = models.CharField(db_column='CON_ENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     dia_est = models.CharField(db_column='DIA_EST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hor_tar = models.CharField(db_column='HOR_TAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cal_tar = models.CharField(db_column='CAL_TAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     exi_esc = models.CharField(db_column='EXI_ESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pre_com = models.CharField(db_column='PRE_COM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pre_ma = models.CharField(db_column='PRE_MA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ma_tar = models.CharField(db_column='MA_TAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ma_falt = models.CharField(db_column='MA_FALT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tran_est = models.CharField(db_column='TRAN_EST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hrs_trab = models.CharField(db_column='HRS_TRAB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     trab_act = models.CharField(db_column='TRAB_ACT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     niv_max = models.CharField(db_column='NIV_MAX', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     no_lic = models.CharField(db_column='NO_LIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     si_lic = models.CharField(db_column='SI_LIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     si_pos = models.CharField(db_column='SI_POS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_dano = models.CharField(db_column='ACT_DANO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_imp = models.CharField(db_column='ACT_IMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_int = models.CharField(db_column='ACT_INT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_ref = models.CharField(db_column='ACT_REF', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_prio = models.CharField(db_column='ACT_PRIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_flim = models.CharField(db_column='ACT_FLIM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_pri = models.CharField(db_column='ACT_PRI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_com = models.CharField(db_column='ACT_COM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_tiem = models.CharField(db_column='ACT_TIEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_apla = models.CharField(db_column='ACT_APLA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     act_impu = models.CharField(db_column='ACT_IMPU', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     des_lim = models.CharField(db_column='DES_LIM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     des_act = models.CharField(db_column='DES_ACT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     des_ord = models.CharField(db_column='DES_ORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ex_op = models.CharField(db_column='EX_OP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pre_exa1 = models.CharField(db_column='PRE_EXA1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     oca_exa = models.CharField(db_column='OCA_EXA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pre_cuen = models.CharField(db_column='PRE_CUEN', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pre_guia = models.CharField(db_column='PRE_GUIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pre_tra = models.CharField(db_column='PRE_TRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pre_cur = models.CharField(db_column='PRE_CUR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_ma = models.CharField(db_column='CON_MA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_pa = models.CharField(db_column='CON_PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_par = models.CharField(db_column='CON_PAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_her = models.CharField(db_column='CON_HER', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_ab = models.CharField(db_column='CON_AB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_hij = models.CharField(db_column='CON_HIJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     con_otr = models.CharField(db_column='CON_OTR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     her_fal = models.CharField(db_column='HER_FAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     lug_her = models.CharField(db_column='LUG_HER', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     her_ma = models.CharField(db_column='HER_MA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     trab_ma = models.CharField(db_column='TRAB_MA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     trab_pa = models.CharField(db_column='TRAB_PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esco_mad = models.CharField(db_column='ESCO_MAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esco_pad = models.CharField(db_column='ESCO_PAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cuan_lib = models.CharField(db_column='CUAN_LIB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     exp_pad = models.CharField(db_column='EXP_PAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     museo = models.CharField(db_column='MUSEO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cine = models.CharField(db_column='CINE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     espec = models.CharField(db_column='ESPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ingr_men = models.CharField(db_column='INGR_MEN', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     apor = models.CharField(db_column='APOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     dep_eco = models.CharField(db_column='DEP_ECO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_alum = models.CharField(db_column='SER_ALUM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_pavi = models.CharField(db_column='SER_PAVI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_basu = models.CharField(db_column='SER_BASU', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_dren = models.CharField(db_column='SER_DREN', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_agua = models.CharField(db_column='SER_AGUA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_tele = models.CharField(db_column='SER_TELE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_mic = models.CharField(db_column='SER_MIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_ref = models.CharField(db_column='SER_REF', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_lav = models.CharField(db_column='SER_LAV', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_inte = models.CharField(db_column='SER_INTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_sus = models.CharField(db_column='SER_SUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_dvd = models.CharField(db_column='SER_DVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_pc = models.CharField(db_column='SER_PC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_tv = models.CharField(db_column='SER_TV', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_auto = models.CharField(db_column='SER_AUTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_mp3 = models.CharField(db_column='SER_MP3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_tec = models.CharField(db_column='SER_TEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ser_calc = models.CharField(db_column='SER_CALC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     vva_rm = models.CharField(db_column='VVA_RM', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     vva_fp = models.CharField(db_column='VVA_FP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     edo_rep = models.CharField(db_column='EDO_REP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uc_cas = models.CharField(db_column='UC_CAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uc_esc = models.CharField(db_column='UC_ESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uc_cc = models.CharField(db_column='UC_CC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uc_caf = models.CharField(db_column='UC_CAF', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uc_cayf = models.CharField(db_column='UC_CAYF', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uc_tra = models.CharField(db_column='UC_TRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_ca = models.CharField(db_column='CH_CA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_ea = models.CharField(db_column='CH_EA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_dev = models.CharField(db_column='CH_DEV', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_ced = models.CharField(db_column='CH_CED', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_hc = models.CharField(db_column='CH_HC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_avhc = models.CharField(db_column='CH_AVHC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_imp = models.CharField(db_column='CH_IMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_int = models.CharField(db_column='CH_INT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_cor = models.CharField(db_column='CH_COR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_bajp = models.CharField(db_column='CH_BAJP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_chat = models.CharField(db_column='CH_CHAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_cmbd = models.CharField(db_column='CH_CMBD', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_di = models.CharField(db_column='CH_DI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_cpw = models.CharField(db_column='CH_CPW', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_hp = models.CharField(db_column='CH_HP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_enva = models.CharField(db_column='CH_ENVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_pmult = models.CharField(db_column='CH_PMULT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ch_rlp = models.CharField(db_column='CH_RLP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ei_p = models.CharField(db_column='EI_P', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ei_s = models.CharField(db_column='EI_S', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ei_bac = models.CharField(db_column='EI_BAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ei_id = models.CharField(db_column='EI_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ei_ex = models.CharField(db_column='EI_EX', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ei_pp = models.CharField(db_column='EI_PP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ei_auto = models.CharField(db_column='EI_AUTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_avb = models.CharField(db_column='LI_AVB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_inf = models.CharField(db_column='LI_INF', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_re = models.CharField(db_column='LI_RE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_inst = models.CharField(db_column='LI_INST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_not = models.CharField(db_column='LI_NOT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_taca = models.CharField(db_column='LI_TACA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_artte = models.CharField(db_column='LI_ARTTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_tere = models.CharField(db_column='LI_TERE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     li_targ = models.CharField(db_column='LI_TARG', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esi_ns = models.CharField(db_column='ESI_NS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esi_infp = models.CharField(db_column='ESI_INFP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esi_tefa = models.CharField(db_column='ESI_TEFA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esi_apex = models.CharField(db_column='ESI_APEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esi_apve = models.CharField(db_column='ESI_APVE', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esi_eny = models.CharField(db_column='ESI_ENY', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esi_ac = models.CharField(db_column='ESI_AC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_ib = models.CharField(db_column='HI_IB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_exs = models.CharField(db_column='HI_EXS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_tnc = models.CharField(db_column='HI_TNC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_dcon = models.CharField(db_column='HI_DCON', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_ap = models.CharField(db_column='HI_AP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_pla = models.CharField(db_column='HI_PLA', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_tdiv = models.CharField(db_column='HI_TDIV', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_ccr = models.CharField(db_column='HI_CCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_esp = models.CharField(db_column='HI_ESP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_contr = models.CharField(db_column='HI_CONTR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_host = models.CharField(db_column='HI_HOST', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hi_lcol = models.CharField(db_column='HI_LCOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_ib = models.CharField(db_column='ESCI_IB', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_nh = models.CharField(db_column='ESCI_NH', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_oaf = models.CharField(db_column='ESCI_OAF', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_ctc = models.CharField(db_column='ESCI_CTC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_ap = models.CharField(db_column='ESCI_AP', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_ept = models.CharField(db_column='ESCI_EPT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_csr = models.CharField(db_column='ESCI_CSR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_con = models.CharField(db_column='ESCI_CON', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_lc = models.CharField(db_column='ESCI_LC', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esci_hos = models.CharField(db_column='ESCI_HOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     numero = models.FloatField(db_column='NUMERO', blank=True, null=True)  # Field name made lowercase.
#     global_field = models.FloatField(db_column='GLOBAL', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
#     percentil = models.FloatField(db_column='PERCENTIL', blank=True, null=True)  # Field name made lowercase.
#     porcne = models.FloatField(db_column='PORCNE', blank=True, null=True)  # Field name made lowercase.
#     p_global = models.FloatField(db_column='P_GLOBAL', blank=True, null=True)  # Field name made lowercase.
#     rv = models.FloatField(db_column='RV', blank=True, null=True)  # Field name made lowercase.
#     rm = models.FloatField(db_column='RM', blank=True, null=True)  # Field name made lowercase.
#     mc = models.FloatField(db_column='MC', blank=True, null=True)  # Field name made lowercase.
#     cn = models.FloatField(db_column='CN', blank=True, null=True)  # Field name made lowercase.
#     cs = models.FloatField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
#     mat = models.FloatField(db_column='MAT', blank=True, null=True)  # Field name made lowercase.
#     esp = models.FloatField(db_column='ESP', blank=True, null=True)  # Field name made lowercase.
#     m1 = models.FloatField(db_column='M1', blank=True, null=True)  # Field name made lowercase.
#     m2 = models.FloatField(db_column='M2', blank=True, null=True)  # Field name made lowercase.
#     m3 = models.FloatField(db_column='M3', blank=True, null=True)  # Field name made lowercase.
#     m4 = models.FloatField(db_column='M4', blank=True, null=True)  # Field name made lowercase.
#     m5 = models.FloatField(db_column='M5', blank=True, null=True)  # Field name made lowercase.
#     m6 = models.FloatField(db_column='M6', blank=True, null=True)  # Field name made lowercase.
#     m7 = models.FloatField(db_column='M7', blank=True, null=True)  # Field name made lowercase.
#     m8 = models.FloatField(db_column='M8', blank=True, null=True)  # Field name made lowercase.
#     m9 = models.FloatField(db_column='M9', blank=True, null=True)  # Field name made lowercase.
#     m10 = models.FloatField(db_column='M10', blank=True, null=True)  # Field name made lowercase.
#     m11 = models.FloatField(db_column='M11', blank=True, null=True)  # Field name made lowercase.
#     m12 = models.FloatField(db_column='M12', blank=True, null=True)  # Field name made lowercase.
#     p_rv = models.FloatField(db_column='P_RV', blank=True, null=True)  # Field name made lowercase.
#     p_rm = models.FloatField(db_column='P_RM', blank=True, null=True)  # Field name made lowercase.
#     p_mc = models.FloatField(db_column='P_MC', blank=True, null=True)  # Field name made lowercase.
#     p_cn = models.FloatField(db_column='P_CN', blank=True, null=True)  # Field name made lowercase.
#     p_cs = models.FloatField(db_column='P_CS', blank=True, null=True)  # Field name made lowercase.
#     p_mat = models.FloatField(db_column='P_MAT', blank=True, null=True)  # Field name made lowercase.
#     p_esp = models.FloatField(db_column='P_ESP', blank=True, null=True)  # Field name made lowercase.
#     p_m1 = models.FloatField(db_column='P_M1', blank=True, null=True)  # Field name made lowercase.
#     p_m2 = models.FloatField(db_column='P_M2', blank=True, null=True)  # Field name made lowercase.
#     p_m3 = models.FloatField(db_column='P_M3', blank=True, null=True)  # Field name made lowercase.
#     p_m4 = models.FloatField(db_column='P_M4', blank=True, null=True)  # Field name made lowercase.
#     p_m5 = models.FloatField(db_column='P_M5', blank=True, null=True)  # Field name made lowercase.
#     p_m6 = models.FloatField(db_column='P_M6', blank=True, null=True)  # Field name made lowercase.
#     p_m7 = models.FloatField(db_column='P_M7', blank=True, null=True)  # Field name made lowercase.
#     p_m8 = models.FloatField(db_column='P_M8', blank=True, null=True)  # Field name made lowercase.
#     p_m9 = models.FloatField(db_column='P_M9', blank=True, null=True)  # Field name made lowercase.
#     p_m10 = models.FloatField(db_column='P_M10', blank=True, null=True)  # Field name made lowercase.
#     p_m11 = models.FloatField(db_column='P_M11', blank=True, null=True)  # Field name made lowercase.
#     p_m12 = models.FloatField(db_column='P_M12', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ceneval_08'


# class CentroCosto(models.Model):
#     cve_centro_costo = models.SmallIntegerField(primary_key=True)
#     clave = models.CharField(max_length=10, blank=True, null=True)
#     clave_alfa = models.CharField(max_length=10, blank=True, null=True)
#     nombre = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'centro_costo'


# class CentroGestor(models.Model):
#     cve_centro_gestor = models.IntegerField(primary_key=True)
#     cve_area = models.SmallIntegerField()
#     numero_centro_gestor = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     area_funcional = models.CharField(max_length=12)
#     encargado = models.BooleanField()
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()
#     cve_jefe = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'centro_gestor'
#         unique_together = (('cve_centro_gestor', 'cve_empleado'),)


# class Ciudad(models.Model):
#     cve_ciudad = models.SmallIntegerField(primary_key=True)
#     cve_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='cve_estado')
#     nombre = models.CharField(max_length=50)
#     lada = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'ciudad'


# class Clase(models.Model):
#     cve_docente = models.ForeignKey('Docente', models.DO_NOTHING, db_column='cve_docente')
#     cve_clase = models.IntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_periodo', blank=True, null=True)
#     cve_materia = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_materia', blank=True, null=True)
#     cve_plan_estudio = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_plan_estudio', blank=True, null=True)
#     cve_carrera = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_carrera', blank=True, null=True)
#     cve_especialidad = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_especialidad', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'clase'
#         unique_together = (('cve_clase', 'cve_docente'),)


# class ClaseIdioma(models.Model):
#     cve_clase_idioma = models.IntegerField(primary_key=True)
#     cve_docente = models.ForeignKey(Clase, models.DO_NOTHING, db_column='cve_docente')
#     cve_docente_idioma = models.CharField(max_length=10)
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo')
#     cve_grupo_idioma = models.IntegerField()
#     cve_clase = models.ForeignKey(Clase, models.DO_NOTHING, db_column='cve_clase')

#     class Meta:
#         managed = False
#         db_table = 'clase_idioma'
#         unique_together = (('cve_clase_idioma', 'cve_docente', 'cve_docente_idioma', 'cve_periodo', 'cve_grupo_idioma', 'cve_clase'),)


# class Cliente(models.Model):
#     cve_cliente = models.IntegerField(primary_key=True)
#     tipo_cliente = models.CharField(max_length=1)

#     class Meta:
#         managed = False
#         db_table = 'cliente'
#         unique_together = (('cve_cliente', 'tipo_cliente'),)


# class ClienteServicio(models.Model):
#     cve_departamento = models.OneToOneField('ServicioPorDepartamento', models.DO_NOTHING, db_column='cve_departamento', primary_key=True)
#     cve_servicio = models.ForeignKey('ServicioPorDepartamento', models.DO_NOTHING, db_column='cve_servicio')
#     cliente = models.CharField(max_length=35)

#     class Meta:
#         managed = False
#         db_table = 'cliente_servicio'
#         unique_together = (('cve_departamento', 'cve_servicio'),)


# class Colonia(models.Model):
#     cve_colonia = models.IntegerField(primary_key=True)
#     cve_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='cve_ciudad')
#     nombre = models.CharField(max_length=50)
#     codigo_postal = models.CharField(max_length=7)

#     class Meta:
#         managed = False
#         db_table = 'colonia'


# class ColoniaFaltante(models.Model):
#     colonia = models.CharField(db_column='Colonia', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ciudad = models.CharField(db_column='Ciudad', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     estado = models.CharField(db_column='Estado', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     cp = models.CharField(db_column='CP', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     registrado = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'colonia_faltante'


# class Combinacion(models.Model):
#     id_combinacion = models.IntegerField(primary_key=True)
#     id_firma = models.IntegerField()
#     orden = models.IntegerField()
#     status_autorizado = models.IntegerField()
#     status_rechazado = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'combinacion'
#         unique_together = (('id_combinacion', 'id_firma'),)


# class ComprobacionGastos(models.Model):
#     cve_comprobacion = models.IntegerField()
#     cve_oficio = models.IntegerField()
#     fecha = models.DateTimeField()
#     lugar = models.CharField(max_length=300)
#     pasaje = models.FloatField()
#     caseta = models.FloatField()
#     taxi = models.FloatField()
#     hospedaje = models.FloatField()
#     desayuno = models.FloatField()
#     comida = models.FloatField()
#     cena = models.FloatField()
#     colegiatura = models.FloatField()
#     viaticos = models.FloatField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'comprobacion_gastos'


# class Concepto(models.Model):
#     cve_concepto = models.IntegerField(primary_key=True)
#     cve_grupo_concepto = models.SmallIntegerField()
#     nombre = models.CharField(max_length=1000)
#     status = models.CharField(max_length=1)
#     monto = models.FloatField()
#     activo = models.BooleanField()
#     id_concepto = models.CharField(max_length=5, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'concepto'


# class ConceptoCuotaDeducible(models.Model):
#     cve_concepto_cuota = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     tipo = models.CharField(max_length=3)
#     nombre_tipo = models.CharField(max_length=50)
#     tipo_concepto = models.CharField(max_length=5)
#     nombre_concepto = models.CharField(max_length=50)
#     cantidad = models.FloatField()
#     dia = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'concepto_cuota_deducible'


# class ConceptoDeducible(models.Model):
#     cve_concepto = models.IntegerField()
#     cve_concepto_cuota = models.IntegerField()
#     fecha_inicio = models.DateTimeField(blank=True, null=True)
#     fecha_fin = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'concepto_deducible'


# class ConceptoPago(models.Model):
#     cve_concepto = models.CharField(primary_key=True, max_length=4)
#     cve_nivel_estudio = models.IntegerField()
#     tipo_pago = models.IntegerField(blank=True, null=True)
#     numero_periodo = models.IntegerField()
#     numero_concepto = models.CharField(max_length=4)
#     concepto = models.CharField(max_length=100)
#     monto = models.FloatField()
#     letra_monto = models.CharField(max_length=400)
#     fecha_limite_pago = models.DateTimeField()
#     cie = models.CharField(max_length=30, blank=True, null=True)
#     activo = models.BooleanField()
#     cve_periodo = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'concepto_pago'


# class ConceptoPagoIndice(models.Model):
#     cve_concepto = models.IntegerField(primary_key=True)
#     cve_concepto_pago = models.CharField(max_length=4)

#     class Meta:
#         managed = False
#         db_table = 'concepto_pago_indice'


# class CondicionPago(models.Model):
#     cve_condicion_pago = models.IntegerField(primary_key=True)
#     cve_proveedor = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     tiempo_entrega = models.CharField(max_length=100)
#     plazo = models.CharField(max_length=150)
#     activo = models.BooleanField()
#     banco = models.CharField(max_length=500)
#     referencia = models.CharField(max_length=500)

#     class Meta:
#         managed = False
#         db_table = 'condicion_pago'


# class CondicionVivienda(models.Model):
#     cve_solicitud_beca = models.ForeignKey('SolicitudBecaInscripcion', models.DO_NOTHING, db_column='cve_solicitud_beca')
#     cve_tipo_solicitud = models.IntegerField()
#     tipo_casa = models.IntegerField()
#     tipo_vivienda = models.IntegerField()
#     material_pared = models.CharField(max_length=25)
#     material_techo = models.CharField(max_length=25)
#     servicios_vivienda = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'condicion_vivienda'


# class Configuracion(models.Model):
#     cve_parametro = models.IntegerField(primary_key=True)
#     parametro = models.CharField(max_length=200)
#     valor = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'configuracion'


# class ConfiguracionCambioCuatrimestre(models.Model):
#     cve_proceso = models.IntegerField()
#     nombre = models.CharField(max_length=200)
#     descripcion = models.CharField(max_length=200)
#     catalogo = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'configuracion_cambio_cuatrimestre'


# class ConfiguracionSistema(models.Model):
#     cve_configuracion = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=600, blank=True, null=True)
#     parametro_bol = models.BooleanField(blank=True, null=True)
#     parametro_int = models.IntegerField(blank=True, null=True)
#     parametro_str = models.CharField(max_length=20, blank=True, null=True)
#     parametro_date1 = models.DateTimeField(blank=True, null=True)
#     parametro_date2 = models.DateTimeField(blank=True, null=True)
#     tipo = models.CharField(max_length=5, blank=True, null=True)
#     visible = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'configuracion_sistema'


# class ConpetenciaCarrera(models.Model):
#     cve_plan_estudio = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()
#     descripcion = models.TextField()  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'conpetencia_carrera'


# class ConsidenciaEmpleo(models.Model):
#     cve_coinsidencia_empleo = models.IntegerField()
#     nombre = models.CharField(max_length=60, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'considencia_empleo'


# class Contacto(models.Model):
#     cve_contacto = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40)
#     apellido_materno = models.CharField(max_length=40)
#     telefono = models.CharField(max_length=20, blank=True, null=True)
#     extencion = models.CharField(max_length=20, blank=True, null=True)
#     mail = models.CharField(max_length=100, blank=True, null=True)
#     celular = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'contacto'


# class ContactoBachillerato(models.Model):
#     cve_contacto = models.IntegerField()
#     cve_puesto = models.IntegerField(blank=True, null=True)
#     cve_bachillerato = models.IntegerField(blank=True, null=True)
#     turno = models.IntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     telefono = models.CharField(max_length=13, blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     extension = models.CharField(max_length=4, blank=True, null=True)
#     celular = models.CharField(max_length=13, blank=True, null=True)
#     casa = models.CharField(max_length=13, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'contacto_bachillerato'


# class ContactoEmpresa(models.Model):
#     cve_empresa = models.IntegerField(primary_key=True)
#     cve_contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='cve_contacto')
#     modulo = models.CharField(max_length=1)

#     class Meta:
#         managed = False
#         db_table = 'contacto_empresa'
#         unique_together = (('cve_empresa', 'cve_contacto'),)


# class ContactoInstitucion(models.Model):
#     cve_contacto = models.IntegerField(primary_key=True)
#     cve_puesto = models.ForeignKey('PuestoInstitucion', models.DO_NOTHING, db_column='cve_puesto')
#     cve_institucion = models.ForeignKey('Institucion', models.DO_NOTHING, db_column='cve_institucion', blank=True, null=True)
#     cve_colonia = models.IntegerField()
#     cve_contacto_recados = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=50, blank=True, null=True)
#     telefono_uno = models.CharField(max_length=50)
#     telefono_dos = models.CharField(max_length=50, blank=True, null=True)
#     extension_uno = models.CharField(max_length=50, blank=True, null=True)
#     extension_dos = models.CharField(max_length=50, blank=True, null=True)
#     fax = models.CharField(max_length=50, blank=True, null=True)
#     email = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField()
#     direccion = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'contacto_institucion'


# class ContactoProveedor(models.Model):
#     cve_contacto = models.IntegerField()
#     cve_proveedor = models.IntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=200)
#     apellido_paterno = models.CharField(max_length=150)
#     apellido_materno = models.CharField(max_length=150, blank=True, null=True)
#     correo_electronico_contacto = models.CharField(max_length=150, blank=True, null=True)
#     id_nextel = models.CharField(max_length=50, blank=True, null=True)
#     telefono = models.CharField(max_length=20, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'contacto_proveedor'


# class ContactoVacante(models.Model):
#     cve_vacante = models.OneToOneField('Vacante', models.DO_NOTHING, db_column='cve_vacante', primary_key=True)
#     cve_empresa = models.ForeignKey('Vacante', models.DO_NOTHING, db_column='cve_empresa')
#     cve_contacto = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'contacto_vacante'
#         unique_together = (('cve_vacante', 'cve_empresa', 'cve_contacto'),)


# class ContraRecibo(models.Model):
#     cve_contra_recibo = models.IntegerField(primary_key=True)
#     cve_cliente = models.IntegerField()
#     tipo_cliente = models.CharField(max_length=1)
#     fecha_elaboracion = models.DateTimeField()
#     fecha_pago = models.DateTimeField()
#     status = models.CharField(max_length=1)
#     numero_cheque = models.CharField(max_length=20, blank=True, null=True)
#     observaciones = models.TextField()  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'contra_recibo'
#         unique_together = (('cve_contra_recibo', 'cve_cliente', 'tipo_cliente'),)


# class ControlCuentaUsuario(models.Model):
#     cve_control = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     usuario = models.CharField(max_length=10)
#     fecha = models.DateTimeField()
#     accion = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'control_cuenta_usuario'


# class ConvenioEstadia(models.Model):
#     folio = models.CharField(primary_key=True, max_length=10)
#     cve_proyecto = models.IntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     cve_periodo = models.SmallIntegerField(blank=True, null=True)
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     fecha_entrega = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'convenio_estadia'


# class Convocatoria(models.Model):
#     cve_convocatoria = models.IntegerField(primary_key=True)
#     cve_encuesta = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     fecha_inicio = models.DateTimeField()
#     fecha_cierre = models.DateTimeField()
#     fecha_publicacion = models.DateTimeField()
#     maximo_beneficiarios = models.IntegerField()
#     documentos = models.CharField(max_length=50)
#     monto_otorgado = models.FloatField()
#     cve_requisito = models.ForeignKey('Requisito', models.DO_NOTHING, db_column='cve_requisito')
#     cve_beca = models.ForeignKey('Requisito', models.DO_NOTHING, db_column='cve_beca')
#     pago_inscripcion = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'convocatoria'


# class ConvocatoriaPersona(models.Model):
#     cve_interesado_convocatoria = models.IntegerField(primary_key=True)
#     cve_fecha_plazo = models.IntegerField()
#     cve_convocatoria = models.IntegerField()
#     localizado = models.BooleanField()
#     interesado = models.BooleanField()
#     entrevista1 = models.BooleanField()
#     fecha1 = models.DateTimeField()
#     entrevista2 = models.BooleanField()
#     fecha2 = models.DateTimeField()
#     calificacion_examen = models.IntegerField()
#     contratado = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'convocatoria_persona'
#         unique_together = (('cve_interesado_convocatoria', 'cve_fecha_plazo', 'cve_convocatoria'),)


# class ConvocatoriaReclutamiento(models.Model):
#     cve_convocatoria = models.IntegerField(primary_key=True)
#     cve_departamento = models.SmallIntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=200, blank=True, null=True)
#     proposito = models.CharField(max_length=1000)
#     funciones = models.CharField(max_length=2000)
#     horario_laboral = models.CharField(max_length=30)
#     sueldo = models.FloatField()
#     formacion_academica = models.CharField(max_length=1000)
#     experiencia = models.CharField(max_length=1000)
#     habilidades = models.CharField(max_length=1000)
#     cve_estado_civil = models.IntegerField(blank=True, null=True)
#     sexo = models.CharField(max_length=3, blank=True, null=True)
#     otros_requisitos = models.CharField(max_length=1500)
#     dias_atencion = models.CharField(max_length=150)
#     fecha_captura = models.DateTimeField()
#     cve_importancia = models.IntegerField()
#     activo = models.BooleanField()
#     documentos = models.CharField(max_length=50)
#     status = models.CharField(max_length=3)
#     sabado = models.BooleanField()
#     ripa = models.BooleanField(blank=True, null=True)
#     tipo_convocatoria = models.CharField(max_length=100, blank=True, null=True)
#     horario_sabado = models.CharField(max_length=150, blank=True, null=True)
#     cve_unidad_academica = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'convocatoria_reclutamiento'


# class CoordinadorCarrera(models.Model):
#     cve_unidad_academica = models.IntegerField()
#     cve_carrera = models.SmallIntegerField()
#     cve_area_academica = models.IntegerField()
#     cve_director_area_academica = models.CharField(max_length=10)
#     cve_especialidad = models.IntegerField()
#     cve_empleado = models.ForeignKey('Docente', models.DO_NOTHING, db_column='cve_empleado')
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'coordinador_carrera'


# class CoordinadorEspecialidad(models.Model):
#     cve_docente = models.CharField(max_length=10, blank=True, null=True)
#     cve_especialidad = models.SmallIntegerField(blank=True, null=True)
#     cve_carrera = models.SmallIntegerField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'coordinador_especialidad'


# class CoordinadorTutoreo(models.Model):
#     cve_coordinador_tutoreo = models.CharField(primary_key=True, max_length=10)
#     activo = models.BooleanField()
#     asistente = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'coordinador_tutoreo'


# class CoordinadorTutoreoTutor(models.Model):
#     cve_coordinador_tutoreo = models.CharField(max_length=10, blank=True, null=True)
#     cve_docente = models.CharField(max_length=10, blank=True, null=True)
#     fecha_asignacion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'coordinador_tutoreo_tutor'


# class CoordinadorUgac(models.Model):
#     cve_ugac = models.SmallIntegerField(blank=True, null=True)
#     cve_docente = models.CharField(max_length=10, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'coordinador_ugac'


# class CorreoInstitucionPersona(models.Model):
#     cve_persona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='cve_persona', primary_key=True)
#     correo_institucional = models.CharField(max_length=60)
#     extension = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'correo_institucion_persona'


# class CorreoInstitucional(models.Model):
#     cve_correo = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     correo = models.CharField(max_length=200)
#     fecha = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'correo_institucional'


# class Cotizacion(models.Model):
#     cve_cotizacion = models.IntegerField(primary_key=True)
#     clave = models.CharField(max_length=10, blank=True, null=True)
#     cve_proveedor = models.IntegerField(blank=True, null=True)
#     fecha = models.DateTimeField()
#     no_pedido = models.CharField(max_length=15, blank=True, null=True)
#     fecha_pedido = models.DateTimeField(blank=True, null=True)
#     orden_compra = models.BooleanField()
#     detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
#     iva = models.FloatField(blank=True, null=True)
#     entrega_fecha = models.CharField(max_length=30, blank=True, null=True)
#     entrega_modo = models.CharField(max_length=30, blank=True, null=True)
#     entrega_pago = models.CharField(max_length=30, blank=True, null=True)
#     recepcion_utl = models.BooleanField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'cotizacion'


# class Criterio(models.Model):
#     cve_criterio = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'criterio'


# class CriterioMateriaPeriodo(models.Model):
#     cve_criterio = models.SmallIntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_periodo')
#     cve_materia = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_materia')
#     cve_plan_estudio = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_plan_estudio')
#     cve_carrera = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_carrera')
#     cve_especialidad = models.ForeignKey('MateriaPlanPeriodo', models.DO_NOTHING, db_column='cve_especialidad')
#     porcentaje = models.SmallIntegerField()
#     no_unidad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'criterio_materia_periodo'
#         unique_together = (('cve_criterio', 'cve_periodo', 'cve_materia', 'cve_plan_estudio', 'cve_carrera', 'cve_especialidad', 'no_unidad'),)


# class CriterioMateriaPeriodoPonderacion(models.Model):
#     cve_periodo = models.IntegerField(primary_key=True)
#     cve_materia = models.IntegerField()
#     cve_plan_estudio = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()
#     porcentaje = models.IntegerField()
#     no_unidad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'criterio_materia_periodo_ponderacion'
#         unique_together = (('cve_periodo', 'cve_materia', 'cve_plan_estudio', 'cve_carrera', 'cve_especialidad', 'no_unidad'),)


# class Cuenta(models.Model):
#     cve_cuenta = models.SmallIntegerField(primary_key=True)
#     cve_centro_costo = models.SmallIntegerField()
#     cve_padre = models.SmallIntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=70)
#     nivel = models.SmallIntegerField()
#     activo = models.BooleanField()
#     id_cuenta = models.CharField(max_length=4, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cuenta'


# class CuentaConcepto(models.Model):
#     cve_cuenta = models.SmallIntegerField(primary_key=True)
#     cve_concepto = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'cuenta_concepto'
#         unique_together = (('cve_cuenta', 'cve_concepto'),)


# class CuentaConcepto1(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'cuenta_concepto1'


# class CuentasProveedor(models.Model):
#     cve_cuenta_proveedor = models.IntegerField()
#     cve_proveedor = models.IntegerField(blank=True, null=True)
#     numero_cuenta = models.CharField(max_length=20)
#     banco = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'cuentas_proveedor'


# class CuestionarioAspirante(models.Model):
#     cve_cuestionario = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'cuestionario_aspirante'


# class Curriculum(models.Model):
#     cve_persona = models.IntegerField(primary_key=True)
#     cve_area_academica = models.SmallIntegerField(blank=True, null=True)
#     cve_nivel_escolar = models.IntegerField()
#     cve_puesto_interes = models.IntegerField(blank=True, null=True)
#     descripcion_escolar = models.CharField(max_length=100)
#     fecha_captura = models.DateTimeField()
#     anios_experiencia = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'curriculum'


# class DatosEscolares(models.Model):
#     cve_interesado = models.IntegerField(primary_key=True)
#     cve_especialidad = models.ForeignKey('EspecialidadBachillerato', models.DO_NOTHING, db_column='cve_especialidad', blank=True, null=True)
#     cve_bachillerato = models.ForeignKey('EspecialidadBachillerato', models.DO_NOTHING, db_column='cve_bachillerato', blank=True, null=True)
#     promedio = models.FloatField()
#     anio_inicio = models.CharField(max_length=4)
#     anio_fin = models.CharField(max_length=4)

#     class Meta:
#         managed = False
#         db_table = 'datos_escolares'


# class DatosEscolaresAspirante(models.Model):
#     cve_aspirante = models.OneToOneField(Aspirante, models.DO_NOTHING, db_column='cve_aspirante', primary_key=True)
#     cve_area_conocimiento = models.SmallIntegerField()
#     cve_bachillerato = models.SmallIntegerField()
#     promedio = models.FloatField()
#     anio_inicio = models.CharField(max_length=4)
#     anio_fin = models.CharField(max_length=4)
#     ceneval = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'datos_escolares_aspirante'


# class DatosEscolaresAspiranteLic(models.Model):
#     cve_aspirante = models.IntegerField(primary_key=True)
#     cve_area_conocimiento = models.IntegerField()
#     cve_bachillerato = models.IntegerField()
#     promedio = models.FloatField()
#     anio_inicio = models.CharField(max_length=4)
#     anio_fin = models.CharField(max_length=4)
#     cve_ut = models.IntegerField()
#     cve_especialidad_ut = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'datos_escolares_aspirante_lic'


# class DatosEscolaresLic(models.Model):
#     cve_interesado = models.IntegerField(primary_key=True)
#     cve_especialidad_ut = models.IntegerField()
#     cve_ut = models.IntegerField()
#     cve_especialidad = models.SmallIntegerField()
#     cve_bachillerato = models.SmallIntegerField()
#     promedio = models.FloatField()
#     anio_inicio = models.CharField(max_length=4)
#     anio_fin = models.CharField(max_length=4)

#     class Meta:
#         managed = False
#         db_table = 'datos_escolares_lic'


# class DatosEscolaresLicProf(models.Model):
#     cve_interesado = models.IntegerField()
#     cve_especialidad_ut = models.IntegerField()
#     cve_ut = models.IntegerField()
#     cve_especialidad = models.SmallIntegerField()
#     cve_bachillerato = models.SmallIntegerField()
#     promedio = models.FloatField()
#     anio_inicio = models.CharField(max_length=4)
#     anio_fin = models.CharField(max_length=4)

#     class Meta:
#         managed = False
#         db_table = 'datos_escolares_lic_prof'


# class DatosMedicos(models.Model):
#     cve_persona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='cve_persona', primary_key=True)
#     cve_tipo_sangre = models.ForeignKey('TipoSangre', models.DO_NOTHING, db_column='cve_tipo_sangre')
#     peso = models.FloatField()
#     estatura = models.FloatField()
#     alergias = models.CharField(max_length=60, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'datos_medicos'


# class DatosMedicosPermiso(models.Model):
#     cve_solicitud = models.OneToOneField('SolicitudPermiso', models.DO_NOTHING, db_column='cve_solicitud', primary_key=True)
#     cve_empleado = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='cve_empleado')
#     folio = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='folio')
#     cve_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='cve_medico', blank=True, null=True)
#     cve_padecimiento = models.ForeignKey('Padecimiento', models.DO_NOTHING, db_column='cve_padecimiento', blank=True, null=True)
#     dias_recomendados = models.IntegerField(blank=True, null=True)
#     observaciones = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'datos_medicos_permiso'
#         unique_together = (('cve_solicitud', 'cve_empleado', 'folio'),)


# class Departamento(models.Model):
#     cve_departamento = models.SmallIntegerField(primary_key=True)
#     cve_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='cve_area')
#     nombre = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'departamento'


# class DepartamentoLiberacion(models.Model):
#     cve_departamento = models.SmallIntegerField()
#     cve_proceso = models.SmallIntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'departamento_liberacion'


# class DescripcionEvento(models.Model):
#     cve_evento = models.IntegerField()
#     descripcion = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'descripcion_evento'


# class DescripcionServicio(models.Model):
#     cve_descripcion = models.IntegerField()
#     cve_tipo = models.IntegerField()
#     cve_medida = models.IntegerField()
#     costo = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'descripcion_servicio'


# class Dia(models.Model):
#     cve_dia = models.IntegerField(primary_key=True)
#     dia = models.CharField(max_length=10, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'dia'


# class DiaHorarioEntradaSalida(models.Model):
#     cve_horario_e_s = models.IntegerField(primary_key=True)
#     cve_dia = models.IntegerField()
#     hora_salida = models.CharField(max_length=50)
#     hora_entrada = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'dia_horario_entrada_salida'
#         unique_together = (('cve_horario_e_s', 'cve_dia'),)


# class DiaInhabil(models.Model):
#     cve_dia_inhabil = models.IntegerField(primary_key=True)
#     fecha_inicio = models.DateTimeField(blank=True, null=True)
#     fecha_fin = models.DateTimeField(blank=True, null=True)
#     tipo = models.CharField(max_length=2, blank=True, null=True)
#     descripcion = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'dia_inhabil'


# class DirectorAreaAcademica(models.Model):
#     cve_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='cve_empleado', blank=True, null=True)
#     cve_unidad_academica = models.IntegerField(blank=True, null=True)
#     cve_area_academica = models.SmallIntegerField(blank=True, null=True)
#     cve_carrera = models.IntegerField(blank=True, null=True)
#     cve_especialidad = models.IntegerField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'director_area_academica'


# class DjangoContentType(models.Model):
#     name = models.CharField(max_length=100)
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.CharField(max_length=27)

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class Docente(models.Model):
#     cve_docente = models.CharField(primary_key=True, max_length=10)
#     activo = models.BooleanField()
#     tipo = models.CharField(max_length=4)

#     class Meta:
#         managed = False
#         db_table = 'docente'


# class DocenteMuestra(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'docente_muestra'


# class Docentecambio(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=7, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'docentecambio'


# class DocentesUgac(models.Model):
#     cve_docente = models.OneToOneField(Docente, models.DO_NOTHING, db_column='cve_docente', primary_key=True)
#     cve_ugac = models.ForeignKey('Ugac', models.DO_NOTHING, db_column='cve_ugac')
#     activo = models.BooleanField()
#     coordinador = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'docentes_ugac'
#         unique_together = (('cve_docente', 'cve_ugac'),)


# class Documento(models.Model):
#     cve_documento = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     original = models.BooleanField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'documento'


# class DocumentoEntregado(models.Model):
#     cve_persona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='cve_persona', primary_key=True)
#     cve_documento = models.IntegerField()
#     cve_proceso = models.IntegerField()
#     observaciones = models.CharField(max_length=250, blank=True, null=True)
#     fecha_entrega = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'documento_entregado'
#         unique_together = (('cve_persona', 'cve_documento', 'cve_proceso'),)


# class DocumentoMaterno(models.Model):
#     cve_solicitud = models.IntegerField(blank=True, null=True)
#     cve_empleado = models.CharField(max_length=7, blank=True, null=True)
#     folio = models.CharField(max_length=10, blank=True, null=True)
#     num_impresion = models.IntegerField(blank=True, null=True)
#     descripcion = models.CharField(max_length=30, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'documento_materno'


# class DocumentoProceso(models.Model):
#     cve_documento = models.IntegerField(primary_key=True)
#     cve_proceso = models.IntegerField()
#     obligado = models.BooleanField()
#     dias_plazo_entrega = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'documento_proceso'
#         unique_together = (('cve_documento', 'cve_proceso'),)


# class Domicilio(models.Model):
#     cve_domicilio = models.IntegerField(primary_key=True)
#     cve_colonia = models.ForeignKey(Colonia, models.DO_NOTHING, db_column='cve_colonia')
#     cve_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='cve_persona', blank=True, null=True)
#     direccion = models.CharField(max_length=100)
#     calle_uno = models.CharField(max_length=100, blank=True, null=True)
#     calle_dos = models.CharField(max_length=100, blank=True, null=True)
#     telefono = models.CharField(max_length=15, blank=True, null=True)
#     alternativo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'domicilio'


# class DomicilioEmpresa(models.Model):
#     cve_domicilio = models.IntegerField(primary_key=True)
#     cve_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='cve_empresa', blank=True, null=True)
#     cve_colonia = models.IntegerField(blank=True, null=True)
#     calle = models.CharField(max_length=200)
#     entre1 = models.CharField(max_length=200)
#     entre2 = models.CharField(max_length=200)
#     telefono = models.CharField(max_length=20, blank=True, null=True)
#     telefono2 = models.CharField(max_length=20, blank=True, null=True)
#     fax = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'domicilio_empresa'


# class DomicilioProveedor(models.Model):
#     cve_domicilio = models.IntegerField()
#     cve_proveedor = models.IntegerField(blank=True, null=True)
#     cve_colonia = models.IntegerField(blank=True, null=True)
#     direccion = models.CharField(max_length=200)
#     telefono = models.CharField(max_length=50)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'domicilio_proveedor'


# class Dtproperties(models.Model):
#     objectid = models.IntegerField(blank=True, null=True)
#     property = models.CharField(max_length=64)
#     value = models.CharField(max_length=255, blank=True, null=True)
#     uvalue = models.CharField(max_length=255, blank=True, null=True)
#     lvalue = models.BinaryField(blank=True, null=True)
#     version = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'dtproperties'
#         unique_together = (('id', 'property'),)


# class EconomiaFamiliar(models.Model):
#     cve_solicitud_beca = models.ForeignKey('SolicitudBecaInscripcion', models.DO_NOTHING, db_column='cve_solicitud_beca')
#     cve_tipo_solicitud = models.IntegerField()
#     persona_dependencia = models.CharField(max_length=20)
#     ingreso_familiar = models.CharField(max_length=100)
#     egreso_familiar = models.CharField(max_length=75)
#     mobiliario_vivienda = models.CharField(max_length=50)
#     vehiculo_motor = models.IntegerField()
#     servicio_medico = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'economia_familiar'


# class Edificio(models.Model):
#     cve_edificio = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=20)
#     activo = models.BooleanField()
#     cve_unidad_academica = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'edificio'


# class Egetsu(models.Model):
#     cve_egetsu = models.IntegerField(primary_key=True)
#     cve_aspirante = models.IntegerField()
#     ceneval1 = models.FloatField()
#     ceneval2 = models.FloatField(blank=True, null=True)
#     ceneval3 = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'egetsu'


# class Egresado(models.Model):
#     matricula = models.OneToOneField(Alumno, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_periodo = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()
#     fecha_acto_recepcional = models.DateTimeField()
#     fecha_expedicion = models.DateTimeField()
#     numero_libro = models.CharField(max_length=6)
#     foja = models.CharField(max_length=6)
#     numero_titulo = models.CharField(max_length=6)
#     impreso = models.BooleanField()
#     liberado = models.BooleanField()
#     status = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'egresado'
#         unique_together = (('matricula', 'cve_periodo', 'cve_carrera', 'cve_especialidad'),)


# class EgresadoCancelado(models.Model):
#     numero_titulo = models.CharField(max_length=5)
#     matricula = models.CharField(max_length=12)
#     cve_periodo = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad = models.IntegerField()
#     fecha_acto_recepcional = models.DateTimeField()
#     fecha_expedicion = models.DateTimeField()
#     numero_libro = models.CharField(max_length=5)
#     foja = models.CharField(max_length=5)
#     motivo_cancelacion = models.CharField(max_length=50)
#     fecha_cancelacion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'egresado_cancelado'


# class Empleado(models.Model):
#     cve_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='cve_persona')
#     cve_empleado = models.CharField(primary_key=True, max_length=10)
#     fecha_ingreso = models.DateTimeField()
#     fecha_isseg = models.DateTimeField(blank=True, null=True)
#     numero_imss = models.CharField(max_length=12, blank=True, null=True)
#     activo = models.BooleanField()
#     cve_unidad_academica = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'empleado'


# class EmpleadoCentroGestor(models.Model):
#     cve_centro_gestor = models.IntegerField(primary_key=True)
#     numero_centro_gestor = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'empleado_centro_gestor'
#         unique_together = (('cve_centro_gestor', 'numero_centro_gestor', 'cve_empleado'),)


# class EmpleadoEscolaridad(models.Model):
#     cve_escolaridad = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10)
#     cve_nivel_escolar = models.IntegerField(blank=True, null=True)
#     descripcion_escolaridad = models.CharField(max_length=100)
#     nombre_institucion = models.CharField(max_length=80)
#     observaciones = models.CharField(max_length=100)
#     fecha_titulo = models.DateTimeField()
#     numero_cedula = models.CharField(max_length=20)
#     status_termino = models.CharField(max_length=3)
#     status_maximo_grado = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'empleado_escolaridad'


# class EmpleadoOficio(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     cve_oficio = models.ForeignKey('OficioComision', models.DO_NOTHING, db_column='cve_oficio')
#     cve_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='cve_empleado')

#     class Meta:
#         managed = False
#         db_table = 'empleado_oficio'


# class EmpleadoPersonaFirmar(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10)
#     nombre = models.CharField(max_length=50)
#     cve_tipo_persona = models.IntegerField()
#     prefijo = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'empleado_persona_firmar'


# class Empresa(models.Model):
#     cve_empresa = models.IntegerField(primary_key=True)
#     cve_sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='cve_sector')
#     cve_tamano = models.ForeignKey('Tamano', models.DO_NOTHING, db_column='cve_tamano')
#     cve_giro = models.ForeignKey('Giro', models.DO_NOTHING, db_column='cve_giro', blank=True, null=True)
#     rfc = models.CharField(max_length=15)
#     nombre = models.CharField(max_length=60)
#     razon_social = models.CharField(max_length=60)
#     pagina_web = models.CharField(max_length=100, blank=True, null=True)
#     fecha_registro = models.DateTimeField()
#     actividad_principal = models.CharField(max_length=150)
#     numero_empleados = models.SmallIntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'empresa'


# class EmpresaTemporal(models.Model):
#     cve_empresa = models.IntegerField(primary_key=True)
#     cve_sector = models.IntegerField()
#     cve_tamano = models.IntegerField()
#     cve_giro = models.SmallIntegerField()
#     rfc = models.CharField(max_length=15)
#     nombre = models.CharField(max_length=60)
#     razon_social = models.CharField(max_length=60)
#     pagina_web = models.CharField(max_length=150)
#     fecha_registro = models.DateTimeField()
#     actividad_principal = models.CharField(max_length=150)
#     numero_empleados = models.SmallIntegerField()
#     domicilio = models.CharField(max_length=450)
#     cve_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='cve_ciudad')
#     nombre_cont = models.CharField(max_length=60)
#     a_paterno_cont = models.CharField(max_length=40)
#     a_materno_cont = models.CharField(max_length=40)
#     puesto = models.CharField(max_length=40, blank=True, null=True)
#     area = models.CharField(max_length=40, blank=True, null=True)
#     tel = models.CharField(max_length=20, blank=True, null=True)
#     ext = models.CharField(max_length=20, blank=True, null=True)
#     mail = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'empresa_temporal'


# class Encuesta(models.Model):
#     cve_encuesta = models.IntegerField(primary_key=True)
#     fecha_registro = models.DateTimeField()
#     nombre = models.CharField(max_length=75)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'encuesta'


# class EncuestaCarrera(models.Model):
#     cve_configuracion = models.IntegerField(primary_key=True)
#     cve_especialidad = models.IntegerField()
#     cve_carrera = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'encuesta_carrera'
#         unique_together = (('cve_configuracion', 'cve_especialidad', 'cve_carrera'),)


# class EncuestaCarreraConfiguracion(models.Model):
#     cve_configuracion = models.IntegerField(primary_key=True)
#     cve_encuesta = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'encuesta_carrera_configuracion'


# class EncuestaConfiguracion(models.Model):
#     cve_encuesta = models.IntegerField(primary_key=True)
#     cve_grupo_seguridad = models.IntegerField()
#     nombre = models.CharField(max_length=250)
#     numero_preguntas = models.IntegerField()
#     tiempo_aplicable = models.IntegerField()
#     descripcion = models.CharField(max_length=350)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'encuesta_configuracion'


# class EncuestaHistorial(models.Model):
#     cve_historial = models.IntegerField(primary_key=True)
#     cve_encuesta = models.IntegerField()
#     cve_persona = models.IntegerField()
#     nombre_persona = models.CharField(max_length=300)
#     fecha_modificacion = models.DateTimeField()
#     proceso = models.CharField(max_length=300)

#     class Meta:
#         managed = False
#         db_table = 'encuesta_historial'


# class EncuestaParametro(models.Model):
#     cve_parametro = models.IntegerField(primary_key=True)
#     cve_encuesta = models.IntegerField()
#     alumno = models.BooleanField()
#     docente = models.BooleanField()
#     fecha_modificacion = models.DateTimeField()
#     direccion = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'encuesta_parametro'


# class EncuestaSatisfaccionEstadia(models.Model):
#     cve_encuestado = models.ForeignKey('Encuestado', models.DO_NOTHING, db_column='cve_encuestado', blank=True, null=True)
#     cve_proyecto = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'encuesta_satisfaccion_estadia'


# class EncuestaSeccion(models.Model):
#     cve_encuesta = models.IntegerField()
#     nombre_seccion = models.CharField(max_length=250, blank=True, null=True)
#     cve_pregunta = models.IntegerField(blank=True, null=True)
#     recordar = models.IntegerField()
#     activo = models.SmallIntegerField(blank=True, null=True)
#     numero_seccion = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'encuesta_seccion'


# class Encuestado(models.Model):
#     cve_encuestado = models.IntegerField(primary_key=True)
#     cve_encuesta = models.ForeignKey(Encuesta, models.DO_NOTHING, db_column='cve_encuesta', blank=True, null=True)
#     cve_persona = models.IntegerField()
#     tipo_persona = models.CharField(max_length=2)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'encuestado'


# class EncuestadoVacante(models.Model):
#     cve_encuestado = models.IntegerField(primary_key=True)
#     cve_encuesta = models.IntegerField()
#     cve_vacante = models.IntegerField()
#     cve_empresa = models.IntegerField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'encuestado_vacante'


# class EntregaArticulo(models.Model):
#     cve_entrega = models.IntegerField(primary_key=True)
#     cve_requisicion = models.IntegerField()
#     cve_articulo = models.IntegerField()
#     fecha = models.DateTimeField(blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     completado = models.BooleanField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     folio = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'entrega_articulo'


# class Entrevista(models.Model):
#     cve_entrevista = models.IntegerField(blank=True, null=True)
#     cve_tutor = models.CharField(max_length=10, blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     cve_motivo_entrevista = models.IntegerField(blank=True, null=True)
#     otro_motivo = models.CharField(max_length=80, blank=True, null=True)
#     fecha_entrevista = models.DateTimeField(blank=True, null=True)
#     observaciones = models.CharField(max_length=1000, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'entrevista'


# class EntrevistaProrroga(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_periodo_solicitud = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     fecha_entrevista = models.DateTimeField(blank=True, null=True)
#     observaciones = models.CharField(max_length=1000, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'entrevista_prorroga'
#         unique_together = (('matricula', 'cve_periodo_solicitud'),)


# class EntrevistadorProrroga(models.Model):
#     cve_empleado = models.CharField(primary_key=True, max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'entrevistador_prorroga'


# class Espacio(models.Model):
#     cve_espacio = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     ubicacion = models.CharField(max_length=10)
#     tipo = models.BooleanField()
#     cve_area_academica = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'espacio'


# class EspacioTecnico(models.Model):
#     cve_tecnico = models.ForeignKey('TecnicoServicio', models.DO_NOTHING, db_column='cve_tecnico', blank=True, null=True)
#     cve_area_espacio = models.ForeignKey(AreaEspacio, models.DO_NOTHING, db_column='cve_area_espacio', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'espacio_tecnico'


# class Especialidad(models.Model):
#     cve_especialidad = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=40)
#     abreviatura = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'especialidad'


# class EspecialidadBachillerato(models.Model):
#     cve_especialidad = models.OneToOneField(Especialidad, models.DO_NOTHING, db_column='cve_especialidad', primary_key=True)
#     cve_bachillerato = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'especialidad_bachillerato'
#         unique_together = (('cve_especialidad', 'cve_bachillerato'),)


# class EspecialidadCarrera(models.Model):
#     cve_especialidad = models.SmallIntegerField(primary_key=True)
#     cve_carrera = models.SmallIntegerField()
#     nombre = models.CharField(max_length=200)
#     activo = models.BooleanField()
#     abreviatura = models.CharField(max_length=5)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'especialidad_carrera'
#         unique_together = (('cve_especialidad', 'cve_carrera'),)


# class EspecialidadCarreraAdmision(models.Model):
#     cve_especialidad = models.OneToOneField(EspecialidadCarrera, models.DO_NOTHING, db_column='cve_especialidad', primary_key=True)
#     cve_carrera = models.ForeignKey(EspecialidadCarrera, models.DO_NOTHING, db_column='cve_carrera')
#     fecha_actualizacion = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=12)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'especialidad_carrera_admision'
#         unique_together = (('cve_especialidad', 'cve_carrera'),)


# class EspecialidadProspecto(models.Model):
#     cve_especialidad = models.IntegerField()
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     tipo = models.CharField(max_length=1, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'especialidad_prospecto'


# class EspecialidadUt(models.Model):
#     cve_especialidad_ut = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     abreviacion = models.CharField(max_length=10, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'especialidad_ut'


# class EspecialidadUtLicenciatura(models.Model):
#     cve_carrera_utl = models.IntegerField()
#     cve_especialidad_carrera_utl = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_unidad_academica = models.IntegerField()
#     activo = models.BooleanField()
#     cve_especialidad_ut = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'especialidad_ut_licenciatura'


# class Estado(models.Model):
#     cve_estado = models.SmallIntegerField(primary_key=True)
#     cve_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='cve_pais')
#     nombre = models.CharField(max_length=40)
#     abreviatura = models.CharField(max_length=4, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'estado'


# class EstadoCivil(models.Model):
#     cve_estado_civil = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=15)

#     class Meta:
#         managed = False
#         db_table = 'estado_civil'


# class EstadoZona(models.Model):
#     cve_estado = models.IntegerField(primary_key=True)
#     tipo_zona = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'estado_zona'


# class EvaluacionCoordinadorTutoreo(models.Model):
#     cve_coordinador_tutoreo = models.CharField(max_length=10)
#     cve_encuestado = models.IntegerField()
#     cve_periodo = models.SmallIntegerField()
#     cve_docente = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'evaluacion_coordinador_tutoreo'


# class EvaluacionSolicitudServicio(models.Model):
#     cve_solicitud_servicio = models.ForeignKey('SolicitudServicio', models.DO_NOTHING, db_column='cve_solicitud_servicio', blank=True, null=True)
#     cve_encuestado = models.ForeignKey(Encuestado, models.DO_NOTHING, db_column='cve_encuestado', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'evaluacion_solicitud_servicio'


# class Evento(models.Model):
#     cve_evento = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     ubicacion = models.CharField(max_length=100)
#     fecha = models.DateTimeField()
#     observaciones = models.CharField(max_length=100)
#     inicio_registro = models.DateTimeField()
#     fin_registro = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'evento'


# class EventoBachillerato(models.Model):
#     cve_bachillerato = models.IntegerField(blank=True, null=True)
#     cve_evento = models.IntegerField(blank=True, null=True)
#     cve_contacto = models.IntegerField(blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'evento_bachillerato'


# class EventoDifusion(models.Model):
#     cve_evento = models.IntegerField(primary_key=True)
#     cve_organizador = models.IntegerField()
#     tipo_organizador = models.BooleanField()
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo', blank=True, null=True)
#     nombre = models.CharField(max_length=255)
#     lugar = models.CharField(max_length=255)
#     objetivo = models.CharField(max_length=1000)
#     fecha = models.DateTimeField()
#     hora_inicio = models.CharField(max_length=5)
#     duracion = models.FloatField()
#     participantes = models.IntegerField(blank=True, null=True)
#     disenio_especial = models.BooleanField(blank=True, null=True)
#     presupuesto = models.FloatField()
#     gasto_real = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'evento_difusion'


# class Examen(models.Model):
#     cve_examen = models.IntegerField(primary_key=True)
#     cve_periodo = models.IntegerField()
#     cve_grupo = models.IntegerField()
#     cve_materia = models.IntegerField()
#     primer = models.CharField(max_length=50)
#     segundo = models.CharField(max_length=50)
#     tercer = models.CharField(max_length=50)
#     recuperacion = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'examen'


# class ExamenAdmision(models.Model):
#     cve_examen_admision = models.SmallIntegerField(primary_key=True)
#     fecha_aplicacion = models.DateTimeField()
#     inicio_ventas = models.DateTimeField()
#     fin_ventas = models.DateTimeField()
#     total_folios = models.SmallIntegerField()
#     cve_periodo = models.IntegerField()
#     activo = models.BooleanField()
#     cve_unidad_academica = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'examen_admision'


# class ExamenAlumno(models.Model):
#     cve_periodo = models.SmallIntegerField()
#     fecha = models.DateTimeField()
#     cve_alumno = models.IntegerField(primary_key=True)
#     matricula = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='matricula')
#     calificacion = models.SmallIntegerField(blank=True, null=True)
#     nivel = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'examen_alumno'
#         unique_together = (('cve_alumno', 'matricula'),)


# class ExamenIngles(models.Model):
#     cve_examen = models.IntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo')
#     total_aspirante = models.IntegerField()
#     fecha_examen = models.DateTimeField()
#     fecha_registro = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'examen_ingles'


# class ExamenMedico(models.Model):
#     cve_examen_medico = models.IntegerField(primary_key=True)
#     cve_aspirante = models.IntegerField(blank=True, null=True)
#     diagnostico_clinico = models.CharField(max_length=500)
#     medidas_recomendada = models.CharField(max_length=500)
#     requiere_seguimiento = models.BooleanField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'examen_medico'


# class ExamenRecuperacion(models.Model):
#     cve_clase = models.IntegerField(primary_key=True)
#     cve_docente = models.CharField(max_length=10)
#     no_examen = models.SmallIntegerField()
#     matricula = models.CharField(max_length=12)
#     evaluador = models.CharField(max_length=10, blank=True, null=True)
#     fecha_limite = models.DateTimeField(blank=True, null=True)
#     unidad_tematica = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'examen_recuperacion'
#         unique_together = (('cve_clase', 'cve_docente', 'no_examen', 'matricula', 'unidad_tematica'),)


# class ExamenRegularizacion(models.Model):
#     cve_clase = models.IntegerField(primary_key=True)
#     cve_docente = models.CharField(max_length=10)
#     no_examen = models.SmallIntegerField()
#     matricula = models.CharField(max_length=12)
#     evaluador = models.CharField(max_length=10, blank=True, null=True)
#     fecha_limite = models.DateTimeField(blank=True, null=True)
#     no_unidad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'examen_regularizacion'
#         unique_together = (('cve_clase', 'cve_docente', 'no_examen', 'matricula', 'no_unidad'),)


# class ExperienciaContacto(models.Model):
#     cve_experiencia = models.IntegerField(primary_key=True)
#     cve_contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='cve_contacto', blank=True, null=True)
#     puesto = models.CharField(max_length=40)
#     area = models.CharField(max_length=40)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'experiencia_contacto'


# class ExperienciaLaboral(models.Model):
#     cve_experiencia_laboral = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     cve_empresa = models.IntegerField(blank=True, null=True)
#     cve_contacto = models.SmallIntegerField(blank=True, null=True)
#     cve_medio_trabajo = models.IntegerField()
#     cve_nivel_jerarquico = models.IntegerField()
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     puesto = models.CharField(max_length=40)
#     sueldo = models.FloatField(blank=True, null=True)
#     area = models.CharField(max_length=40)
#     actividades = models.CharField(max_length=255)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'experiencia_laboral'


# class ExploracionFisica(models.Model):
#     cve_exploracion_fisica = models.IntegerField(primary_key=True)
#     cve_examen_medico = models.ForeignKey(ExamenMedico, models.DO_NOTHING, db_column='cve_examen_medico', blank=True, null=True)
#     peso = models.CharField(max_length=10)
#     talla = models.CharField(max_length=10)
#     fc = models.CharField(max_length=10)
#     ta_sistolica = models.CharField(max_length=10)
#     ta_diastolica = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'exploracion_fisica'


# class ExploracionPartesCuerpo(models.Model):
#     cve_exploracion_fisica = models.ForeignKey(ExploracionFisica, models.DO_NOTHING, db_column='cve_exploracion_fisica', blank=True, null=True)
#     cve_parte_cuerpo = models.ForeignKey('PartesCuerpoExamenMedico', models.DO_NOTHING, db_column='cve_parte_cuerpo', blank=True, null=True)
#     normal = models.BooleanField()
#     observacion = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'exploracion_partes_cuerpo'


# class FacturaExterna(models.Model):
#     cve_contra_recibo = models.IntegerField(primary_key=True)
#     cve_cliente = models.IntegerField()
#     tipo_cliente = models.CharField(max_length=1)
#     numero_factura = models.CharField(max_length=30)
#     fecha = models.DateTimeField()
#     total = models.FloatField()
#     observaciones = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'factura_externa'
#         unique_together = (('cve_contra_recibo', 'cve_cliente', 'tipo_cliente', 'numero_factura'),)


# class FacturaUtl(models.Model):
#     cve_factura = models.IntegerField(primary_key=True)
#     cve_transaccion = models.ForeignKey('Transaccion', models.DO_NOTHING, db_column='cve_transaccion', blank=True, null=True)
#     fecha = models.DateTimeField()
#     status = models.CharField(max_length=1)
#     fecha_pago = models.DateTimeField()
#     memo = models.CharField(max_length=50, blank=True, null=True)
#     observaciones = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'factura_utl'


# class FamiliaMaterial(models.Model):
#     cve_familia = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=150)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'familia_material'


# class FechaEstadia(models.Model):
#     cve_fecha_estadia = models.IntegerField(primary_key=True)
#     cve_unidad_academica = models.ForeignKey('UnidadAcademica', models.DO_NOTHING, db_column='cve_unidad_academica')
#     fecha_inicio = models.DateTimeField()
#     fecha_entrega = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'fecha_estadia'


# class FechaExamen(models.Model):
#     cve_fecha_examen = models.IntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo')
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'fecha_examen'


# class FechaPlazoConvocatoria(models.Model):
#     cve_fecha_plazo = models.IntegerField(primary_key=True)
#     cve_convocatoria = models.IntegerField()
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     enviada = models.BooleanField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'fecha_plazo_convocatoria'
#         unique_together = (('cve_fecha_plazo', 'cve_convocatoria'),)


# class FechasBachillerato(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=8000, blank=True, null=True)  # Field name made lowercase.
#     col005 = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fechas_bachillerato'


# class FichaAdmision(models.Model):
#     folio_ceneval = models.CharField(primary_key=True, max_length=10)
#     cve_ficha = models.IntegerField()
#     cve_solicitud_admision = models.SmallIntegerField()
#     folio_pago = models.CharField(max_length=10)
#     cve_examen_admision = models.SmallIntegerField(blank=True, null=True)
#     cve_aspirante = models.IntegerField(blank=True, null=True)
#     cve_examen_aplicacion = models.ForeignKey(ExamenAdmision, models.DO_NOTHING, db_column='cve_examen_aplicacion', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ficha_admision'
#         unique_together = (('folio_ceneval', 'cve_ficha', 'cve_solicitud_admision'),)


# class FichaAdmisionLic(models.Model):
#     cve_ficha = models.IntegerField(primary_key=True)
#     cve_solicitud_admision = models.SmallIntegerField()
#     folio_pago = models.CharField(max_length=10)
#     cve_examen_admision = models.SmallIntegerField(blank=True, null=True)
#     cve_aspirante = models.IntegerField(blank=True, null=True)
#     cve_examen_aplicacion = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ficha_admision_lic'
#         unique_together = (('cve_ficha', 'cve_solicitud_admision'),)


# class FichaExamenAdmision(models.Model):
#     cve_persona = models.IntegerField(primary_key=True)
#     folio_recibo = models.CharField(max_length=10)
#     folio_ceneval = models.CharField(max_length=10, blank=True, null=True)
#     cve_fecha_examen = models.ForeignKey(FechaExamen, models.DO_NOTHING, db_column='cve_fecha_examen')
#     ficha = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'ficha_examen_admision'
#         unique_together = (('cve_persona', 'folio_recibo'),)


# class Firma(models.Model):
#     id_firma = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'firma'


# class FirmaCombinacion(models.Model):
#     id_firma_combinacion = models.IntegerField(primary_key=True)
#     id_combinacion = models.IntegerField()
#     id_firma = models.IntegerField()
#     id_firma_proceso = models.IntegerField()
#     id_modulo = models.IntegerField()
#     fecha = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=10)
#     observaciones = models.CharField(max_length=100)
#     status_anterior = models.CharField(max_length=3)
#     status_actual = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'firma_combinacion'


# class FirmaConvocatoria(models.Model):
#     cve_convocatoria = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     tipo_firma = models.CharField(max_length=4)
#     cve_area_departamento = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'firma_convocatoria'


# class FirmaEmpleado(models.Model):
#     id_firma = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'firma_empleado'
#         unique_together = (('id_firma', 'cve_empleado'),)


# class FirmaProceso(models.Model):
#     id_firma_proceso = models.IntegerField(primary_key=True)
#     id_combinacion = models.IntegerField()
#     proceso = models.CharField(max_length=4)
#     sub_proceso = models.CharField(max_length=4)
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'firma_proceso'


# class FirmasOficio(models.Model):
#     cve_firma = models.IntegerField(primary_key=True)
#     cve_oficio = models.ForeignKey('OficioComision', models.DO_NOTHING, db_column='cve_oficio')
#     firmas_requerida = models.IntegerField()
#     firmas_obtenida = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'firmas_oficio'
#         unique_together = (('cve_firma', 'cve_oficio'),)


# class FirmasOficiosSeguimiento(models.Model):
#     cve_firma = models.IntegerField(primary_key=True)
#     cve_oficio = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     cve_tipo_firma = models.IntegerField()
#     concecutivo = models.IntegerField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'firmas_oficios_seguimiento'
#         unique_together = (('cve_firma', 'cve_oficio', 'cve_empleado', 'cve_tipo_firma'),)


# class Folio(models.Model):
#     fecha = models.DateTimeField(primary_key=True)
#     cve_unidad_academica = models.IntegerField()
#     folio_recibo = models.IntegerField()
#     folio_factura = models.IntegerField()
#     folio_donativo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'folio'
#         unique_together = (('fecha', 'cve_unidad_academica'),)


# class FormacionAcademica(models.Model):
#     cve_formacion = models.IntegerField()
#     cve_persona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='cve_persona', primary_key=True)
#     cve_titulo = models.SmallIntegerField(blank=True, null=True)
#     cve_institucion = models.SmallIntegerField(blank=True, null=True)
#     cedula = models.CharField(max_length=15, blank=True, null=True)
#     fecha_titulo = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'formacion_academica'
#         unique_together = (('cve_persona', 'cve_formacion'),)


# class FotografiaPersona(models.Model):
#     cve_persona = models.IntegerField()
#     foto = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'fotografia_persona'


# class G7(models.Model):
#     cve_empleado = models.CharField(primary_key=True, max_length=12)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'g7'


# class Generacion(models.Model):
#     cve_generacion = models.IntegerField(primary_key=True)
#     cve_periodo_inicio = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo_inicio')
#     cve_periodo_fin = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo_fin')
#     tipo = models.CharField(max_length=1)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'generacion'


# class Giro(models.Model):
#     cve_giro_padre = models.IntegerField()
#     cve_giro = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=80)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'giro'


# class GiroPadre(models.Model):
#     cve_giro_padre = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=40)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'giro_padre'


# class Grupo(models.Model):
#     cve_grupo = models.SmallIntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo', blank=True, null=True)
#     cve_especialidad = models.SmallIntegerField()
#     cve_carrera = models.SmallIntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=10)
#     numero_cuatrimestre = models.SmallIntegerField()
#     cve_turno = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'grupo'

# class GrupoAtendido(models.Model):
#     cve_grupo_atendido = models.IntegerField()
#     cve_bachillerato = models.IntegerField()
#     cve_especialidad = models.IntegerField()
#     turno = models.IntegerField(blank=True, null=True)
#     generacion_inicio = models.IntegerField(blank=True, null=True)
#     generacion_fin = models.IntegerField(blank=True, null=True)
#     numero_alumnos = models.IntegerField(blank=True, null=True)
#     grado = models.IntegerField(blank=True, null=True)
#     grupo = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'grupo_atendido'


# class GrupoConcepto(models.Model):
#     cve_grupo_concepto = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_concepto'


# class GrupoDirigido(models.Model):
#     cve_grupo_dirigido = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     tipo = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_dirigido'


# class GrupoDirigidoPersona(models.Model):
#     cve_grupo_dirigido = models.IntegerField(primary_key=True)
#     cve_grupo_seguridad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_dirigido_persona'
#         unique_together = (('cve_grupo_dirigido', 'cve_grupo_seguridad'),)


# class GrupoIdioma(models.Model):
#     cve_grupo_idioma = models.OneToOneField('self', models.DO_NOTHING, db_column='cve_grupo_idioma', primary_key=True)
#     cve_periodo = models.SmallIntegerField()
#     cve_nivel = models.SmallIntegerField()
#     nombre = models.CharField(max_length=50)
#     cve_turno = models.IntegerField()
#     capacidad = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_idioma'


# class GrupoIngles(models.Model):
#     cve_grupo_ingles = models.IntegerField(primary_key=True)
#     cve_periodo = models.SmallIntegerField()
#     cve_carrera = models.SmallIntegerField()
#     nombre = models.CharField(max_length=50)
#     nivel = models.SmallIntegerField()
#     cve_turno = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_ingles'


# class GrupoInstitucion(models.Model):
#     cve_grupo_institucion = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_institucion'


# class GrupoOptativa(models.Model):
#     cve_grupo_optativa = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     nombre = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'grupo_optativa'


# class GrupoPlanEstudioHorarios(models.Model):
#     cve_grupo_plan_estudio = models.IntegerField(primary_key=True)
#     cve_grupo = models.IntegerField()
#     cve_plan_estudio = models.IntegerField()
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_plan_estudio_horarios'


# class GrupoSeguridad(models.Model):
#     cve_grupo_seguridad = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=40)
#     tiempo_sesion = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'grupo_seguridad'


# class Habilidad(models.Model):
#     cve_habilidad = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     habilidad_padre = models.IntegerField()
#     activo = models.BooleanField()
#     observacion = models.CharField(max_length=200)

#     class Meta:
#         managed = False
#         db_table = 'habilidad'


# class HabilidadPersonaCurriculum(models.Model):
#     cve_habilidad = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     nivel = models.IntegerField()
#     experiencia = models.IntegerField()
#     observacion = models.CharField(max_length=200)
#     porcentaje = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'habilidad_persona_curriculum'
#         unique_together = (('cve_habilidad', 'cve_persona'),)


# class HistorialAsignacionResponsable(models.Model):
#     cve_responsable = models.IntegerField()
#     cve_centro_gestor = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_registro_historial = models.DateTimeField()
#     fecha_inicio = models.DateTimeField()
#     fecha_termino = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'historial_asignacion_responsable'


# class HistorialFechaContrato(models.Model):
#     cve_historial = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10)
#     cve_departamento = models.SmallIntegerField()
#     cve_tipo_puesto = models.SmallIntegerField()
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     consecutivo_plaza = models.IntegerField()
#     status_plaza = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'historial_fecha_contrato'
#         unique_together = (('cve_historial', 'cve_empleado'),)


# class HistorialLaboralEgresado(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_empresa = models.ForeignKey(ContactoEmpresa, models.DO_NOTHING, db_column='cve_empresa')
#     cve_contacto = models.ForeignKey(ContactoEmpresa, models.DO_NOTHING, db_column='cve_contacto', blank=True, null=True)
#     cve_periodo = models.SmallIntegerField(blank=True, null=True)
#     cve_carrera = models.IntegerField(blank=True, null=True)
#     cve_especialidad = models.IntegerField(blank=True, null=True)
#     fecha_ingreso = models.DateTimeField(blank=True, null=True)
#     fecha_termino = models.DateTimeField(blank=True, null=True)
#     motivo_termino = models.CharField(max_length=50, blank=True, null=True)
#     cve_medio_trabajo = models.IntegerField(blank=True, null=True)
#     cve_coinsidencia_empleo = models.IntegerField(blank=True, null=True)
#     cve_tipo_contrato = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'historial_laboral_egresado'
#         unique_together = (('matricula', 'cve_empresa'),)


# class HistorialPago(models.Model):
#     cve_pago = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     referencia = models.CharField(max_length=30)
#     transaccion = models.CharField(max_length=30)
#     concepto = models.CharField(max_length=10)
#     monto = models.CharField(max_length=20)
#     no_control = models.CharField(max_length=15)
#     fecha_referencia = models.CharField(max_length=10)
#     monto_referencia = models.CharField(max_length=10)
#     fecha_pago = models.DateTimeField()
#     lugar_pago = models.CharField(max_length=30)
#     status_pago = models.CharField(max_length=30)
#     num_recibo = models.CharField(max_length=30)
#     cuenta_contable = models.CharField(max_length=30)

#     class Meta:
#         managed = False
#         db_table = 'historial_pago'


# class HistorialStatusAlumno(models.Model):
#     cve_historial = models.IntegerField(primary_key=True)
#     matricula = models.CharField(max_length=12)
#     status = models.CharField(max_length=2)
#     fecha = models.DateTimeField()
#     observacion = models.CharField(max_length=60)

#     class Meta:
#         managed = False
#         db_table = 'historial_status_alumno'


# class HistoricoRegistroTabla(models.Model):
#     cve_historico = models.IntegerField(primary_key=True)
#     clave_tabla_int = models.IntegerField()
#     clave_tabla_str = models.CharField(max_length=15, blank=True, null=True)
#     nombre_tabla = models.CharField(max_length=100)
#     cve_empleado = models.CharField(max_length=10)
#     descripcion = models.CharField(max_length=500)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'historico_registro_tabla'


# class Hora(models.Model):
#     cve_hora = models.SmallIntegerField(primary_key=True)
#     cve_turno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='cve_turno')
#     hora_inicio = models.DateTimeField()
#     hora_fin = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'hora'


# class HoraTipo(models.Model):
#     cve_hora_tipo = models.IntegerField(primary_key=True)
#     cve_tipo_horario = models.IntegerField()
#     no_hora = models.IntegerField()
#     hora_inicio = models.CharField(max_length=50)
#     hora_fin = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'hora_tipo'


# class Horario(models.Model):
#     cve_horario = models.IntegerField(primary_key=True)
#     cve_solicitud = models.ForeignKey(CambioHorario, models.DO_NOTHING, db_column='cve_solicitud')
#     cve_empleado = models.ForeignKey(CambioHorario, models.DO_NOTHING, db_column='cve_empleado')
#     folio = models.ForeignKey(CambioHorario, models.DO_NOTHING, db_column='folio')
#     cve_dia = models.ForeignKey(CatalogoHorario, models.DO_NOTHING, db_column='cve_dia')
#     cve_catalogo_horario = models.ForeignKey(CatalogoHorario, models.DO_NOTHING, db_column='cve_catalogo_horario')
#     activo = models.BooleanField(blank=True, null=True)
#     valido = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'horario'
#         unique_together = (('cve_horario', 'cve_empleado'),)


# class HorarioClase(models.Model):
#     cve_docente = models.CharField(max_length=10)
#     cve_clase = models.IntegerField()
#     cve_aula = models.ForeignKey(AulaSerch, models.DO_NOTHING, db_column='cve_aula')
#     cve_hora = models.ForeignKey(Hora, models.DO_NOTHING, db_column='cve_hora', blank=True, null=True)
#     dia_semana = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'horario_clase'


# class HorarioEntradaSalida(models.Model):
#     cve_horario_e_s = models.IntegerField(primary_key=True)
#     cve_docente = models.CharField(max_length=50)
#     cve_periodo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'horario_entrada_salida'


# class HorarioGrupo(models.Model):
#     cve_horario = models.IntegerField(primary_key=True)
#     cve_materia = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_espacio = models.IntegerField()
#     cve_grupo = models.IntegerField()
#     cve_hora_tipo = models.IntegerField()
#     dia = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_modificacion = models.DateTimeField()
#     fecha_impresion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'horario_grupo'


# class HorarioIngles(models.Model):
#     cve_horario = models.IntegerField()
#     hora_inicio = models.CharField(max_length=6)
#     hora_fin = models.CharField(max_length=6)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'horario_ingles'


# class Image(models.Model):
#     periodo_banner = models.CharField(max_length=15, blank=True, null=True)
#     cve_periodo = models.IntegerField(blank=True, null=True)
#     ruta = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'image'


# class ImagenSolicitud(models.Model):
#     cve_imagen = models.IntegerField()
#     cve_servicio = models.IntegerField()
#     cve_solicitud = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     observaciones = models.CharField(max_length=250, blank=True, null=True)
#     autorizada = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'imagen_solicitud'


# class Inacistencia(models.Model):
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     cve_docente = models.CharField(max_length=10, blank=True, null=True)
#     cve_clase = models.IntegerField(blank=True, null=True)
#     cla_cve_docente = models.CharField(max_length=10, blank=True, null=True)
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'inacistencia'


# class Incidencia(models.Model):
#     cve_incidencia = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'incidencia'


# class IncidenciaAlumno(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_incidencia = models.SmallIntegerField()
#     consecutivo = models.IntegerField()
#     fecha = models.DateTimeField()
#     comentarios = models.CharField(max_length=1000, blank=True, null=True)
#     tipo_observacion = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'incidencia_alumno'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_incidencia', 'consecutivo'),)


# class IncidenciaGrupal(models.Model):
#     cve_grupo = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_incidencia = models.IntegerField()
#     consecutivo = models.IntegerField()
#     fecha = models.DateTimeField(blank=True, null=True)
#     comentarios = models.CharField(max_length=1000, blank=True, null=True)
#     tipo_observacion = models.BooleanField()
#     descripcion = models.CharField(max_length=1000, blank=True, null=True)
#     cve_clase = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'incidencia_grupal'


# class IncidenciaGrupo(models.Model):
#     cve_incidencia = models.IntegerField()
#     nombre = models.CharField(max_length=60, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'incidencia_grupo'


# class InformacionComplementariaAspirante(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     cve_aspirante = models.ForeignKey(Aspirante, models.DO_NOTHING, db_column='cve_aspirante')
#     nombre_madre = models.CharField(max_length=50)
#     apaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     amaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     trabaja = models.BooleanField()
#     cve_tipo_seguro = models.ForeignKey('TipoSeguroSocial', models.DO_NOTHING, db_column='cve_tipo_seguro')
#     referencia_pago = models.CharField(max_length=20, blank=True, null=True)
#     cve_examen_ingles = models.IntegerField(blank=True, null=True)
#     numero_reprogramacion = models.IntegerField(blank=True, null=True)
#     monto = models.FloatField(blank=True, null=True)
#     fecha_pago = models.DateTimeField(blank=True, null=True)
#     seguro_social = models.CharField(max_length=16, blank=True, null=True)
#     tramite_utl = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'informacion_complementaria_aspirante'


# class InformacionComplementariaAspiranteLic(models.Model):
#     cve_registro = models.IntegerField()
#     cve_aspirante = models.IntegerField()
#     nombre_madre = models.CharField(max_length=50)
#     apaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     amaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     trabaja = models.BooleanField()
#     cve_tipo_seguro = models.IntegerField()
#     referencia_pago = models.CharField(max_length=20, blank=True, null=True)
#     cve_examen_ingles = models.IntegerField(blank=True, null=True)
#     numero_reprogramacion = models.IntegerField(blank=True, null=True)
#     monto = models.FloatField(blank=True, null=True)
#     fecha_pago = models.DateTimeField(blank=True, null=True)
#     seguro_social = models.CharField(max_length=15, blank=True, null=True)
#     tramite_utl = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'informacion_complementaria_aspirante_lic'


# class InformacionComplementariaAspiranteLicProf(models.Model):
#     cve_registro = models.IntegerField()
#     cve_aspirante = models.IntegerField()
#     nombre_madre = models.CharField(max_length=50)
#     apaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     amaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     trabaja = models.BooleanField()
#     cve_tipo_seguro = models.IntegerField()
#     referencia_pago = models.CharField(max_length=20, blank=True, null=True)
#     cve_examen_ingles = models.IntegerField(blank=True, null=True)
#     numero_reprogramacion = models.IntegerField(blank=True, null=True)
#     monto = models.FloatField(blank=True, null=True)
#     fecha_pago = models.DateTimeField(blank=True, null=True)
#     seguro_social = models.CharField(max_length=15, blank=True, null=True)
#     tramite_utl = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'informacion_complementaria_aspirante_lic_prof'


# class InformacionComplementariaInteresado(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     cve_interesado = models.ForeignKey('Interesado', models.DO_NOTHING, db_column='cve_interesado', blank=True, null=True)
#     nombre_madre = models.CharField(max_length=50)
#     apaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     amaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     trabaja = models.BooleanField()
#     cve_tipo_seguro = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'informacion_complementaria_interesado'


# class InformacionComplementariaInteresadoLic(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     cve_interesado = models.IntegerField(blank=True, null=True)
#     nombre_madre = models.CharField(max_length=50)
#     apaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     amaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     trabaja = models.BooleanField()
#     cve_tipo_seguro = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'informacion_complementaria_interesado_lic'


# class InformacionComplementariaInteresadoLicProf(models.Model):
#     cve_registro = models.IntegerField()
#     cve_interesado = models.IntegerField(blank=True, null=True)
#     nombre_madre = models.CharField(max_length=50)
#     apaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     amaterno_madre = models.CharField(max_length=50, blank=True, null=True)
#     trabaja = models.BooleanField()
#     cve_tipo_seguro = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'informacion_complementaria_interesado_lic_prof'


# class InicioClases(models.Model):
#     cve_inicio_clases = models.IntegerField()
#     cve_unidad_academica = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_especialidad_carrera = models.IntegerField()
#     cve_director_area = models.CharField(max_length=50)
#     cve_coordinador_carrera = models.CharField(max_length=50)
#     fecha_inicio = models.DateTimeField()
#     hora_inicio = models.CharField(max_length=30, blank=True, null=True)
#     presentarse = models.CharField(max_length=255)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'inicio_clases'


# class Inscripcion(models.Model):
#     matricula = models.OneToOneField(Alumno, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo')
#     fecha_pago = models.DateTimeField()
#     status = models.CharField(max_length=2, blank=True, null=True)
#     referencia_pago1 = models.CharField(max_length=38, blank=True, null=True)
#     referencia_pago2 = models.CharField(max_length=38, blank=True, null=True)
#     monto = models.FloatField(blank=True, null=True)
#     cie = models.CharField(db_column='CIE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     impreso = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'inscripcion'
#         unique_together = (('matricula', 'cve_periodo', 'fecha_pago'),)


# class InscripcionEspecial(models.Model):
#     matricula = models.CharField(max_length=12)
#     cve_periodo = models.SmallIntegerField()
#     fecha_pago = models.DateTimeField()
#     status = models.CharField(max_length=1)
#     referencia_pago1 = models.CharField(max_length=20, blank=True, null=True)
#     referencia_pago2 = models.CharField(max_length=20, blank=True, null=True)
#     monto = models.FloatField(blank=True, null=True)
#     cie = models.CharField(db_column='CIE', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'inscripcion_especial'


# class InscripcionFechaPagos(models.Model):
#     cve_unidad_academica = models.IntegerField(primary_key=True)
#     cve_periodo = models.IntegerField()
#     inicio_pagos = models.DateTimeField()
#     fin_pag_desc = models.DateTimeField()
#     fin_pag_norm = models.DateTimeField()
#     ter_pag_reca = models.DateTimeField()
#     aut_escolares = models.BooleanField()
#     aut_becas = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'inscripcion_fecha_pagos'
#         unique_together = (('cve_unidad_academica', 'cve_periodo'),)


# class InscripcionMontosPagos(models.Model):
#     cve_unidad_academica = models.IntegerField(primary_key=True)
#     cve_periodo = models.IntegerField()
#     pronto_pago = models.FloatField()
#     normal = models.FloatField()
#     beca = models.FloatField()
#     recargo_dia = models.FloatField()
#     cie_normal = models.CharField(db_column='CIE_normal', max_length=50)  # Field name made lowercase.
#     cie_beca = models.CharField(db_column='CIE_beca', max_length=50)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'inscripcion_montos_pagos'
#         unique_together = (('cve_unidad_academica', 'cve_periodo'),)


# class Institucion(models.Model):
#     cve_institucion = models.OneToOneField('InstitucionGrupoInstitucion', models.DO_NOTHING, db_column='cve_institucion', primary_key=True)
#     cve_sector = models.IntegerField()
#     cve_tamano = models.ForeignKey('Tamano', models.DO_NOTHING, db_column='cve_tamano')
#     cve_giro = models.SmallIntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=200)
#     direccion = models.CharField(max_length=200)
#     pagina_web = models.CharField(max_length=250)
#     email = models.CharField(max_length=100)
#     telefono = models.CharField(max_length=20)
#     fecha = models.DateTimeField(blank=True, null=True)
#     cve_colonia = models.IntegerField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     nombre_director = models.CharField(max_length=60, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'institucion'


# class InstitucionGrupoInstitucion(models.Model):
#     cve_institucion = models.IntegerField(primary_key=True)
#     cve_grupo_institucion = models.ForeignKey(GrupoInstitucion, models.DO_NOTHING, db_column='cve_grupo_institucion', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'institucion_grupo_institucion'


# class Instrucciones(models.Model):
#     cve_encuesta = models.ForeignKey(Encuesta, models.DO_NOTHING, db_column='cve_encuesta', blank=True, null=True)
#     instrucciones = models.CharField(max_length=800, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fitro = models.CharField(max_length=800, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'instrucciones'


# class Interesado(models.Model):
#     cve_interesado = models.IntegerField(primary_key=True)
#     cve_solicitud_admision = models.ForeignKey('SolicitudAdmision', models.DO_NOTHING, db_column='cve_solicitud_admision', blank=True, null=True)
#     cve_promotor = models.ForeignKey('Promotor', models.DO_NOTHING, db_column='cve_promotor', blank=True, null=True)
#     fecha_registro = models.DateTimeField()
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=40, blank=True, null=True)
#     cve_pais = models.IntegerField(blank=True, null=True)
#     cve_ciudad = models.IntegerField(blank=True, null=True)
#     cve_colonia = models.IntegerField()
#     direccion = models.CharField(max_length=100)
#     cve_estado_civil = models.IntegerField(blank=True, null=True)
#     rfc = models.CharField(max_length=15)
#     curp = models.CharField(max_length=18, blank=True, null=True)
#     sexo = models.CharField(max_length=1)
#     fecha_nacimiento = models.DateTimeField()
#     mail = models.CharField(max_length=60, blank=True, null=True)
#     telefono = models.CharField(max_length=15, blank=True, null=True)
#     movil = models.CharField(max_length=20, blank=True, null=True)
#     nombre_tutor = models.CharField(max_length=100)
#     edad_tutor = models.DateTimeField(blank=True, null=True)
#     telefono_tutor = models.CharField(max_length=15, blank=True, null=True)
#     cve_cuestionario = models.IntegerField()
#     medio_registro = models.CharField(max_length=20)
#     nacimiento_extranjero = models.CharField(max_length=50, blank=True, null=True)
#     cve_estado = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'interesado'


# class InteresadoConvocatoria(models.Model):
#     cve_interesado_convocatoria = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     tipo_persona = models.CharField(max_length=3)

#     class Meta:
#         managed = False
#         db_table = 'interesado_convocatoria'


# class InteresadoLic(models.Model):
#     cve_interesado = models.IntegerField(primary_key=True)
#     cve_solicitud_admision = models.SmallIntegerField()
#     cve_promotor = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateTimeField()
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=40, blank=True, null=True)
#     cve_pais = models.IntegerField(blank=True, null=True)
#     cve_ciudad = models.IntegerField(blank=True, null=True)
#     cve_colonia = models.IntegerField()
#     direccion = models.CharField(max_length=100)
#     cve_estado_civil = models.IntegerField(blank=True, null=True)
#     rfc = models.CharField(max_length=15)
#     curp = models.CharField(max_length=18, blank=True, null=True)
#     sexo = models.CharField(max_length=1)
#     fecha_nacimiento = models.DateTimeField()
#     mail = models.CharField(max_length=60, blank=True, null=True)
#     telefono = models.CharField(max_length=15, blank=True, null=True)
#     movil = models.CharField(max_length=20, blank=True, null=True)
#     nombre_tutor = models.CharField(max_length=100)
#     edad_tutor = models.DateTimeField(blank=True, null=True)
#     telefono_tutor = models.CharField(max_length=15, blank=True, null=True)
#     cve_cuestionario = models.IntegerField()
#     medio_registro = models.CharField(max_length=20)
#     nacimiento_extranjero = models.CharField(max_length=50, blank=True, null=True)
#     cve_estado = models.SmallIntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'interesado_lic'


# class InteresadoLicProf(models.Model):
#     cve_interesado = models.IntegerField(primary_key=True)
#     cve_solicitud_admision = models.SmallIntegerField()
#     cve_promotor = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateTimeField()
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=40, blank=True, null=True)
#     cve_pais = models.IntegerField(blank=True, null=True)
#     cve_ciudad = models.IntegerField(blank=True, null=True)
#     cve_colonia = models.IntegerField()
#     direccion = models.CharField(max_length=100)
#     cve_estado_civil = models.IntegerField(blank=True, null=True)
#     rfc = models.CharField(max_length=15)
#     curp = models.CharField(max_length=18, blank=True, null=True)
#     sexo = models.CharField(max_length=1)
#     fecha_nacimiento = models.DateTimeField()
#     mail = models.CharField(max_length=60, blank=True, null=True)
#     telefono = models.CharField(max_length=15, blank=True, null=True)
#     movil = models.CharField(max_length=20, blank=True, null=True)
#     nombre_tutor = models.CharField(max_length=100)
#     edad_tutor = models.DateTimeField(blank=True, null=True)
#     telefono_tutor = models.CharField(max_length=15, blank=True, null=True)
#     cve_cuestionario = models.IntegerField()
#     medio_registro = models.CharField(max_length=20)
#     nacimiento_extranjero = models.CharField(max_length=50, blank=True, null=True)
#     cve_estado = models.SmallIntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'interesado_lic_prof'


# class IntervencionIndividual(models.Model):
#     cve_intervencion_individual = models.IntegerField(primary_key=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     cve_grupo = models.SmallIntegerField(blank=True, null=True)
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     cve_tipo_entrevista_psicopedagogico = models.IntegerField(blank=True, null=True)
#     aplicacion_de_pruebas = models.BooleanField(blank=True, null=True)
#     respuesta_canalizacion = models.TextField(blank=True, null=True)  # This field type is a guess.
#     atencion_a_padres = models.BooleanField(blank=True, null=True)
#     observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.
#     fecha = models.DateTimeField(blank=True, null=True)
#     cve_coordinador_tutoreo = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'intervencion_individual'


# class IntervencionIndividualSesion(models.Model):
#     cve_intervencion_individual_sesion = models.AutoField(primary_key=True)
#     cve_intervencion_individual = models.IntegerField()
#     fecha = models.DateTimeField()
#     observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'intervencion_individual_sesion'


# class IntervencionMotivoPsicopedagogico(models.Model):
#     cve_intervencion_motivo_psicopedagogico = models.AutoField(primary_key=True)
#     cve_intervencion_individual = models.IntegerField()
#     cve_catalogo_motivo_psicopedagogico = models.IntegerField()
#     principal = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'intervencion_motivo_psicopedagogico'


# class Invitado(models.Model):
#     cve_invitado = models.IntegerField(primary_key=True)
#     cve_contacto = models.ForeignKey(ContactoInstitucion, models.DO_NOTHING, db_column='cve_contacto')
#     cve_tipo_invitado = models.ForeignKey('TipoInvitado', models.DO_NOTHING, db_column='cve_tipo_invitado')
#     cve_representante = models.IntegerField()
#     jerarquia = models.IntegerField()
#     observaciones = models.CharField(max_length=50, blank=True, null=True)
#     cve_status_invitado = models.ForeignKey('StatusInvitado', models.DO_NOTHING, db_column='cve_status_invitado')
#     motivo_invitacion = models.CharField(max_length=255, blank=True, null=True)
#     enviar_mensaje = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'invitado'


# class InvitadoListaInvitados(models.Model):
#     cve_lista_invitados = models.ForeignKey('ListaInvitados', models.DO_NOTHING, db_column='cve_lista_invitados', blank=True, null=True)
#     cve_invitado = models.ForeignKey(Invitado, models.DO_NOTHING, db_column='cve_invitado', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'invitado_lista_invitados'


# class JerarquiaEmpleadoOficio(models.Model):
#     cve_jerarquia = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'jerarquia_empleado_oficio'
#         unique_together = (('cve_jerarquia', 'cve_persona'),)


# class JerarquiaOficio(models.Model):
#     cve_jerarquia = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=250)
#     relevancia = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'jerarquia_oficio'


# class LiberacionAlumno(models.Model):
#     cve_departamento = models.SmallIntegerField(primary_key=True)
#     cve_servicio = models.IntegerField()
#     cve_especialidad = models.SmallIntegerField()
#     cve_carrera = models.SmallIntegerField()
#     cve_proceso = models.SmallIntegerField()
#     matricula = models.CharField(max_length=12)
#     status = models.BooleanField()
#     observacion = models.CharField(max_length=500)
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'liberacion_alumno'
#         unique_together = (('cve_departamento', 'cve_servicio', 'cve_especialidad', 'cve_carrera', 'cve_proceso', 'matricula'),)


# class LiberacionHorario(models.Model):
#     cve_liberacion_horario = models.IntegerField(primary_key=True)
#     cve_carrera = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     liberado = models.BooleanField()
#     cve_empleado = models.CharField(max_length=50)
#     fecha_liberacion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'liberacion_horario'


# class LiberadorAlumno(models.Model):
#     cve_liberador = models.IntegerField(primary_key=True)
#     cve_departamento = models.SmallIntegerField(blank=True, null=True)
#     cve_servicio = models.IntegerField(blank=True, null=True)
#     cve_especialidad = models.SmallIntegerField(blank=True, null=True)
#     cve_carrera = models.SmallIntegerField(blank=True, null=True)
#     cve_proceso = models.SmallIntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     status = models.BooleanField(blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)
#     observacion = models.CharField(max_length=500, blank=True, null=True)
#     cve_empleado = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'liberador_alumno'


# class LiberadorServicio(models.Model):
#     cve_departamento = models.OneToOneField('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_departamento', primary_key=True)
#     cve_servicio = models.ForeignKey('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_servicio')
#     cve_especialidad = models.ForeignKey('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_especialidad')
#     cve_carrera = models.ForeignKey('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_carrera')
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'liberador_servicio'
#         unique_together = (('cve_departamento', 'cve_servicio', 'cve_especialidad', 'cve_carrera', 'cve_empleado'),)


# class Licencia(models.Model):
#     cve_solicitud = models.OneToOneField('SolicitudPermiso', models.DO_NOTHING, db_column='cve_solicitud', primary_key=True)
#     cve_empleado = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='cve_empleado')
#     folio = models.ForeignKey('SolicitudPermiso', models.DO_NOTHING, db_column='folio')
#     cve_tabulador = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'licencia'
#         unique_together = (('cve_solicitud', 'cve_empleado', 'folio'),)


# class ListaInvitados(models.Model):
#     cve_lista_invitados = models.IntegerField(primary_key=True)
#     cve_evento = models.ForeignKey(EventoDifusion, models.DO_NOTHING, db_column='cve_evento')
#     fecha = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'lista_invitados'


# class ListaPreeliminarIngles(models.Model):
#     cve_lista = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     cve_grupo_ingles = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     cve_horario = models.IntegerField()
#     cve_aula = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'lista_preeliminar_ingles'


# class Materia(models.Model):
#     cve_materia = models.IntegerField(primary_key=True)
#     cve_area_conocimiento = models.ForeignKey(AreaConocimiento, models.DO_NOTHING, db_column='cve_area_conocimiento', blank=True, null=True)
#     nombre = models.CharField(max_length=100)
#     abreviatura = models.CharField(max_length=5, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'materia'


# class MateriaExtracurricular(models.Model):
#     cve_materia = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     corto = models.CharField(max_length=10)
#     no_horas = models.IntegerField()
#     activo = models.BooleanField()
#     num_cuatrimestre = models.IntegerField()
#     cve_plan_estudio = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'materia_extracurricular'


# class MateriaPlanEstudio(models.Model):
#     cve_materia = models.IntegerField(primary_key=True)
#     cve_plan_estudio = models.ForeignKey('PlanEstudio', models.DO_NOTHING, db_column='cve_plan_estudio')
#     cve_carrera = models.ForeignKey('PlanEstudio', models.DO_NOTHING, db_column='cve_carrera')
#     cve_especialidad = models.ForeignKey('PlanEstudio', models.DO_NOTHING, db_column='cve_especialidad')
#     no_cuatrimestre = models.SmallIntegerField()
#     no_unidades = models.IntegerField()
#     folio_materia = models.CharField(max_length=20)
#     no_horas_semana = models.FloatField(blank=True, null=True)
#     integradora = models.BooleanField(blank=True, null=True)
#     estadia = models.BooleanField(blank=True, null=True)
#     extracurricular = models.BooleanField()
#     faltas = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'materia_plan_estudio'
#         unique_together = (('cve_materia', 'cve_plan_estudio', 'cve_carrera', 'cve_especialidad'),)


# class MateriaPlanPeriodo(models.Model):
#     cve_periodo = models.OneToOneField('Periodo', models.DO_NOTHING, db_column='cve_periodo', primary_key=True)
#     cve_materia = models.ForeignKey(MateriaPlanEstudio, models.DO_NOTHING, db_column='cve_materia')
#     cve_plan_estudio = models.ForeignKey(MateriaPlanEstudio, models.DO_NOTHING, db_column='cve_plan_estudio')
#     cve_carrera = models.ForeignKey(MateriaPlanEstudio, models.DO_NOTHING, db_column='cve_carrera')
#     cve_especialidad = models.ForeignKey(MateriaPlanEstudio, models.DO_NOTHING, db_column='cve_especialidad')

#     class Meta:
#         managed = False
#         db_table = 'materia_plan_periodo'
#         unique_together = (('cve_periodo', 'cve_materia', 'cve_plan_estudio', 'cve_carrera', 'cve_especialidad'),)


# class MateriaPlanPeriodoOptativa(models.Model):
#     cve_optativa = models.IntegerField(primary_key=True)
#     cve_periodo = models.SmallIntegerField()
#     cve_materia = models.IntegerField()
#     cve_plan_estudio = models.SmallIntegerField()
#     cve_carrera = models.SmallIntegerField()
#     cve_especialidad = models.SmallIntegerField()
#     cve_materia_optativa = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'materia_plan_periodo_optativa'


# class MateriaRevalidada(models.Model):
#     folio_revalidadacion = models.IntegerField()
#     cve_materia = models.IntegerField()
#     cve_plan_estudio = models.SmallIntegerField()
#     cve_carrera = models.SmallIntegerField()
#     cve_especialidad = models.SmallIntegerField()
#     calificacion = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'materia_revalidada'


# class MateriaUgac(models.Model):
#     cve_materia = models.IntegerField()
#     cve_ugac = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'materia_ugac'


# class MaterialServicio(models.Model):
#     cve_material = models.IntegerField(primary_key=True)
#     cve_familia = models.ForeignKey(FamiliaMaterial, models.DO_NOTHING, db_column='cve_familia', blank=True, null=True)
#     cve_partida = models.ForeignKey('Partida', models.DO_NOTHING, db_column='cve_partida')
#     id = models.CharField(max_length=20, blank=True, null=True)
#     descripcion = models.CharField(max_length=100)
#     costo_unitario = models.FloatField(blank=True, null=True)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'material_servicio'


# class MaterialSolicitudServicio(models.Model):
#     cve_solicitud_servicio = models.ForeignKey('TecnicoSolicitudServicio', models.DO_NOTHING, db_column='cve_solicitud_servicio', blank=True, null=True)
#     cve_tecnico = models.ForeignKey('TecnicoSolicitudServicio', models.DO_NOTHING, db_column='cve_tecnico', blank=True, null=True)
#     cve_material = models.ForeignKey(MaterialServicio, models.DO_NOTHING, db_column='cve_material', blank=True, null=True)
#     comentarios = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'material_solicitud_servicio'


# class Medico(models.Model):
#     cve_medico = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     apellido_paterno = models.CharField(max_length=200, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=200, blank=True, null=True)
#     telefono1 = models.CharField(max_length=20)
#     telefono2 = models.CharField(max_length=20, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'medico'


# class MedidaDescripcion(models.Model):
#     cve_medida = models.IntegerField()
#     precio = models.FloatField(blank=True, null=True)
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'medida_descripcion'


# class MedioTrabajo(models.Model):
#     cve_medio_trabajo = models.IntegerField()
#     nombre = models.CharField(max_length=60)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'medio_trabajo'


# class MedioTransporteOficio(models.Model):
#     cve_medio_transporte = models.IntegerField()
#     cve_oficio = models.IntegerField(primary_key=True)
#     cve_tipo_vehiculo = models.IntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=50)
#     placas = models.CharField(max_length=20)
#     km_estimado = models.IntegerField()
#     vales_solicitado = models.IntegerField()
#     vales_autorizado = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'medio_transporte_oficio'


# class MejorPromedio(models.Model):
#     lugar = models.IntegerField()
#     matricula = models.CharField(max_length=12)
#     fecha_evento = models.DateTimeField()
#     promedio = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'mejor_promedio'


# class Mensaje(models.Model):
#     cve_mensaje = models.IntegerField(primary_key=True)
#     cve_grupo_dirigido = models.IntegerField()
#     titulo = models.CharField(max_length=50)
#     descripcion = models.TextField()  # This field type is a guess.
#     cve_remitente = models.CharField(max_length=20)
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     nivel_prioridad = models.IntegerField()
#     activo = models.BooleanField()
#     fecha_publicacion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'mensaje'
#         unique_together = (('cve_mensaje', 'cve_grupo_dirigido'),)


# class MensajeAlumno(models.Model):
#     cve_mensaje = models.IntegerField(primary_key=True)
#     cve_grupo = models.IntegerField()
#     matricula = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'mensaje_alumno'


# class MensajeDocente(models.Model):
#     cve_mensaje = models.IntegerField(primary_key=True)
#     cve_docente = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'mensaje_docente'


# class MensajeEmpleado(models.Model):
#     cve_mensaje = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'mensaje_empleado'


# class MensajeGeneral(models.Model):
#     cve_mensaje = models.IntegerField(primary_key=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'mensaje_general'


# class MensajeLeido(models.Model):
#     cve_mensaje = models.IntegerField(primary_key=True)
#     cve_usuario = models.CharField(max_length=20)

#     class Meta:
#         managed = False
#         db_table = 'mensaje_leido'


# class MensajeTutor(models.Model):
#     cve_mensaje = models.IntegerField(primary_key=True)
#     cve_docente = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'mensaje_tutor'


# class Migrations(models.Model):
#     migration = models.CharField(max_length=255)
#     batch = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'migrations'


# class ModalidadTemaPpg(models.Model):
#     cve_modalidad_tema_ppg = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'modalidad_tema_ppg'


# class Modulo(models.Model):
#     cve_modulo = models.IntegerField(primary_key=True)
#     cve_padre = models.IntegerField()
#     nombre = models.CharField(max_length=60)
#     ruta = models.CharField(max_length=100, blank=True, null=True)
#     visible = models.BooleanField()
#     orden = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'modulo'


# class ModuloAccesoExclusivo(models.Model):
#     cve_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='cve_modulo')
#     ip = models.CharField(max_length=15)

#     class Meta:
#         managed = False
#         db_table = 'modulo_acceso_exclusivo'


# class ModuloPadre(models.Model):
#     cve_modulo = models.IntegerField(primary_key=True)
#     valor = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'modulo_padre'


# class ModuloPermiso(models.Model):
#     cve_grupo_seguridad = models.OneToOneField(GrupoSeguridad, models.DO_NOTHING, db_column='cve_grupo_seguridad', primary_key=True)
#     cve_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='cve_modulo')

#     class Meta:
#         managed = False
#         db_table = 'modulo_permiso'
#         unique_together = (('cve_grupo_seguridad', 'cve_modulo'),)


# class ModuloServicio(models.Model):
#     cve_modulo = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'modulo_servicio'


# class ModuloServicioEncuesta(models.Model):
#     cve_modulo = models.IntegerField()
#     cve_encuesta = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'modulo_servicio_encuesta'


# class Motivo(models.Model):
#     cve_motivo = models.IntegerField(primary_key=True)
#     motivo = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo'


# class MotivoBaja(models.Model):
#     cve_motivo_baja = models.SmallIntegerField(primary_key=True)
#     cve_tipo = models.ForeignKey('TipoBaja', models.DO_NOTHING, db_column='cve_tipo')
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_baja'
#         unique_together = (('cve_motivo_baja', 'cve_tipo'),)


# class MotivoBajaEmpleado(models.Model):
#     cve_motivo_baja = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_baja_empleado'


# class MotivoCalifiacionTardia(models.Model):
#     cve_motivo = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_califiacion_tardia'


# class MotivoCalificacionTardia(models.Model):
#     cve_motivo = models.SmallIntegerField()
#     nombre = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_calificacion_tardia'


# class MotivoCambioCalificacion(models.Model):
#     cve_motivo = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_cambio_calificacion'


# class MotivoCambioCalificacionRemedial(models.Model):
#     cve_motivo = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=300)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_cambio_calificacion_remedial'


# class MotivoCancelacionBeca(models.Model):
#     cve_motivo = models.IntegerField(primary_key=True)
#     motivo = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_cancelacion_beca'


# class MotivoEntrevista(models.Model):
#     cve_motivo_entrevista = models.IntegerField()
#     nombre = models.CharField(max_length=80, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'motivo_entrevista'


# class MotivoNoExamen(models.Model):
#     cve_persona = models.IntegerField()
#     cve_tipo_motivo = models.IntegerField(blank=True, null=True)
#     motivo = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'motivo_no_examen'


# class MotivoNoInscripcion(models.Model):
#     cve_persona = models.IntegerField()
#     cve_tipo_motivo = models.IntegerField()
#     motivo = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'motivo_no_inscripcion'


# class MotivoPermiso(models.Model):
#     cve_permiso = models.OneToOneField('Permiso', models.DO_NOTHING, db_column='cve_permiso', primary_key=True)
#     cve_motivo = models.ForeignKey(Motivo, models.DO_NOTHING, db_column='cve_motivo')
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'motivo_permiso'
#         unique_together = (('cve_permiso', 'cve_motivo'),)


# class MotivoProrroga(models.Model):
#     cve_motivo = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=30)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'motivo_prorroga'


# class Movimiento(models.Model):
#     cve_movimiento = models.IntegerField(primary_key=True)
#     cve_transaccion = models.IntegerField()
#     cve_cuenta = models.SmallIntegerField(blank=True, null=True)
#     cve_concepto = models.IntegerField(blank=True, null=True)
#     cantidad = models.SmallIntegerField()
#     monto_unitario = models.FloatField()
#     monto_total = models.FloatField()
#     tipo_movimiento = models.CharField(max_length=1)
#     descuento = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'movimiento'


# class Naturaleza(models.Model):
#     cve_naturaleza = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=80)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'naturaleza'


# class NivelEscolar(models.Model):
#     cve_nivel_escolar = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     abreviatura = models.CharField(max_length=10)
#     activo = models.BooleanField()
#     nivel = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'nivel_escolar'


# class NivelEspacio(models.Model):
#     cve_nivel_espacio = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     nomenclatura = models.CharField(max_length=20, blank=True, null=True)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'nivel_espacio'


# class NivelEstudio(models.Model):
#     cve_nivel_estudio = models.SmallIntegerField()
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'nivel_estudio'


# class NivelIdioma(models.Model):
#     cve_nivel = models.IntegerField(primary_key=True)
#     descripcion = models.TextField()  # This field type is a guess.
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'nivel_idioma'


# class NivelIngles(models.Model):
#     cve_nivel = models.IntegerField()
#     nivel = models.IntegerField()
#     acierto_minimo = models.IntegerField()
#     acierto_maximo = models.IntegerField()
#     descripcion = models.CharField(max_length=50)
#     libro = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'nivel_ingles'


# class NivelJerarquico(models.Model):
#     cve_nivel_jerarquico = models.IntegerField()
#     nombre = models.CharField(max_length=60, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nivel_jerarquico'


# class NoSeguro(models.Model):
#     matricula = models.CharField(max_length=255, blank=True, null=True)
#     no = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'no__seguro'


# class Nocontar(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'nocontar'


# class NombrePuesto(models.Model):
#     cve_nombre_puesto = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'nombre_puesto'


# class OauthAccessTokens(models.Model):
#     id = models.CharField(primary_key=True, max_length=100)
#     user_id = models.BigIntegerField(blank=True, null=True)
#     client_id = models.BigIntegerField()
#     name = models.CharField(max_length=255, blank=True, null=True)
#     scopes = models.TextField(blank=True, null=True)
#     revoked = models.BooleanField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     expires_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oauth_access_tokens'


# class OauthAuthCodes(models.Model):
#     id = models.CharField(primary_key=True, max_length=100)
#     user_id = models.BigIntegerField()
#     client_id = models.BigIntegerField()
#     scopes = models.TextField(blank=True, null=True)
#     revoked = models.BooleanField()
#     expires_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oauth_auth_codes'


# class OauthClients(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user_id = models.BigIntegerField(blank=True, null=True)
#     name = models.CharField(max_length=255)
#     secret = models.CharField(max_length=100, blank=True, null=True)
#     provider = models.CharField(max_length=255, blank=True, null=True)
#     redirect = models.TextField()
#     personal_access_client = models.BooleanField()
#     password_client = models.BooleanField()
#     revoked = models.BooleanField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oauth_clients'


# class OauthPersonalAccessClients(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     client_id = models.BigIntegerField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oauth_personal_access_clients'


# class OauthRefreshTokens(models.Model):
#     id = models.CharField(primary_key=True, max_length=100)
#     access_token_id = models.CharField(max_length=100)
#     revoked = models.BooleanField()
#     expires_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oauth_refresh_tokens'


# class ObjetivoOficioComision(models.Model):
#     cve_objetivo = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     objetivo = models.CharField(max_length=255)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'objetivo_oficio_comision'


# class ObjetivosOficio(models.Model):
#     cve_oficio = models.IntegerField(primary_key=True)
#     cve_objetivo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'objetivos_oficio'


# class ObservacionFormatoEscolar(models.Model):
#     cve_observacion = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=1000)
#     cve_empleado = models.CharField(max_length=10)
#     cve_empleado_actualizacion = models.CharField(max_length=10)
#     fecha_registro = models.DateTimeField()
#     fecha_actualizacion = models.DateTimeField()
#     matricula = models.CharField(max_length=10)
#     tipo_formato = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'observacion_formato_escolar'


# class OficioComision(models.Model):
#     cve_oficio = models.OneToOneField('self', models.DO_NOTHING, db_column='cve_oficio', primary_key=True)
#     numero_centro_gestor = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     centro_gestor_oficio = models.IntegerField()
#     numero_oficio = models.IntegerField()
#     descripcion_oficio = models.CharField(max_length=1300)
#     institucion = models.CharField(max_length=200)
#     cve_ciudad = models.IntegerField()
#     fecha_inicio = models.DateTimeField()
#     hora_inicio = models.CharField(max_length=10)
#     fecha_termino = models.DateTimeField()
#     hora_termino = models.CharField(max_length=10)
#     fecha_registro = models.DateTimeField()
#     cve_empleado_registro = models.CharField(max_length=10)
#     cve_destino = models.IntegerField()
#     cve_oficio_anexo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'oficio_comision'


# class OficioNoAutorizacion(models.Model):
#     cve_no_autorizacion = models.IntegerField()
#     cve_oficio = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     motivo = models.CharField(max_length=255)
#     tipo_persona = models.SmallIntegerField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'oficio_no_autorizacion'


# class OpcionListaPreliminar(models.Model):
#     matricula = models.OneToOneField(Alumno, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='cve_periodo')
#     pago_asistencia = models.SmallIntegerField(blank=True, null=True)
#     motivo = models.SmallIntegerField(blank=True, null=True)
#     observaciones = models.CharField(max_length=200, blank=True, null=True)
#     retro = models.CharField(max_length=200, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'opcion_lista_preliminar'
#         unique_together = (('matricula', 'cve_periodo'),)


# class OtorgamientoViatico(models.Model):
#     cve_otorgamiento = models.IntegerField(primary_key=True)
#     cve_oficio = models.IntegerField()
#     tipo_otorgamiento = models.CharField(max_length=2)
#     cve_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='cve_empleado')
#     fecha_registro = models.DateTimeField()
#     numero_registro = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'otorgamiento_viatico'


# class OtraCarrera(models.Model):
#     cve_carrera = models.IntegerField()
#     nombre = models.CharField(max_length=250, blank=True, null=True)
#     status = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'otra_carrera'


# class OtraCarreraUniversidad(models.Model):
#     cve_universidad = models.IntegerField(blank=True, null=True)
#     cve_carrera = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'otra_carrera_universidad'


# class OtraUniversidad(models.Model):
#     cve_universidad = models.IntegerField()
#     nombre = models.CharField(max_length=250, blank=True, null=True)
#     status = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'otra_universidad'


# class OtrosViaticosOficio(models.Model):
#     cve_viatico = models.IntegerField(primary_key=True)
#     cve_oficio = models.ForeignKey(OficioComision, models.DO_NOTHING, db_column='cve_oficio')
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=255)
#     importe_solicitado = models.FloatField()
#     importe_autorizado = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'otros_viaticos_oficio'
#         unique_together = (('cve_viatico', 'cve_oficio'),)


# class Padecimiento(models.Model):
#     cve_padecimiento = models.IntegerField(primary_key=True)
#     padecimiento = models.CharField(max_length=200)
#     observaciones = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'padecimiento'


# class PadecimientoExamenMedico(models.Model):
#     cve_examen_medico = models.ForeignKey(ExamenMedico, models.DO_NOTHING, db_column='cve_examen_medico', blank=True, null=True)
#     cve_padecimiento = models.IntegerField(blank=True, null=True)
#     opcion = models.BooleanField()
#     observacion = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'padecimiento_examen_medico'


# class PadecimientoMujer(models.Model):
#     cve_padecimiento = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     fecha_registro = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'padecimiento_mujer'


# class PadecimientoPersonal(models.Model):
#     cve_persona = models.ForeignKey(DatosMedicos, models.DO_NOTHING, db_column='cve_persona')
#     cve_padecimiento = models.IntegerField()
#     padece = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'padecimiento_personal'


# class PagosCaja(models.Model):
#     fecha = models.CharField(max_length=255, blank=True, null=True)
#     mat_alur = models.CharField(db_column='mat_aluR', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     total = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pagos_caja'


# class PagosLinea(models.Model):
#     s_transm = models.CharField(max_length=20, blank=True, null=True)
#     c_referencia = models.CharField(max_length=25, blank=True, null=True)
#     val_1 = models.IntegerField(blank=True, null=True)
#     t_servicio = models.IntegerField(blank=True, null=True)
#     t_importe = models.FloatField(blank=True, null=True)
#     val_3 = models.IntegerField(blank=True, null=True)
#     t_pago = models.CharField(max_length=4, blank=True, null=True)
#     n_autoriz = models.CharField(max_length=40, blank=True, null=True)
#     val_9 = models.CharField(max_length=10, blank=True, null=True)
#     val_10 = models.CharField(max_length=40, blank=True, null=True)
#     val_5 = models.IntegerField(blank=True, null=True)
#     val_6 = models.CharField(max_length=20, blank=True, null=True)
#     val_11 = models.CharField(max_length=30, blank=True, null=True)
#     val_12 = models.CharField(max_length=30, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pagos_linea'


# class Pagosa(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'pagosa'


# class Pais(models.Model):
#     cve_pais = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     nacionalidad = models.CharField(max_length=40)
#     abreviatura = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pais'


# class Parentesco(models.Model):
#     cve_parentesco = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=30)

#     class Meta:
#         managed = False
#         db_table = 'parentesco'


# class PartesCuerpoExamenMedico(models.Model):
#     cve_parte_cuerpo = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     fecha_registro = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'partes_cuerpo_examen_medico'


# class Partida(models.Model):
#     cve_partida = models.IntegerField(primary_key=True)
#     cve_subcapitulo = models.ForeignKey('Subcapitulo', models.DO_NOTHING, db_column='cve_subcapitulo')
#     nombre = models.CharField(max_length=200)
#     descripcion = models.CharField(max_length=1000)
#     activo = models.BooleanField()
#     clave = models.CharField(max_length=4)

#     class Meta:
#         managed = False
#         db_table = 'partida'


# class PercentilesTemporal(models.Model):
#     cve_aspirante = models.IntegerField(blank=True, null=True)
#     posicion = models.IntegerField(blank=True, null=True)
#     fecha_inscripcion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'percentiles_temporal'


# class PerfilPuestoInteres(models.Model):
#     cve_puesto_interes = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=70)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'perfil_puesto_interes'


class Periodo(models.Model):
    cve_periodo = models.SmallIntegerField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    fecha_inicio_clases = models.DateTimeField()
    fecha_fin_clases = models.DateTimeField()
    numero_periodo = models.IntegerField()
    no_extras = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField()

    def get_periodo_name(self):
        return f"{self.fecha_inicio.strftime('%B')} - {self.fecha_fin.strftime('%B')} {self.fecha_inicio.year}"

    class Meta:
        managed = False
        db_table = 'periodo'

    def __str__(self):
        return f"{self.fecha_inicio.strftime('%B')} - {self.fecha_fin.strftime('%B')} {self.fecha_inicio.year}"
    

# class PeriodoCapturaCalificacion(models.Model):
#     cve_periodo_captura = models.IntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='cve_periodo')
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     fecha_limite_captura_normal = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'periodo_captura_calificacion'


# class PeriodoCapturaEstadia(models.Model):
#     cve_periodo_captura = models.IntegerField()
#     cve_periodo = models.SmallIntegerField()
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     numero_parcial = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'periodo_captura_estadia'


# class PeriodoProyectoEmpresa(models.Model):
#     cve_proyecto_empresa = models.OneToOneField('ProyectoEstadiaEmpresa', models.DO_NOTHING, db_column='cve_proyecto_empresa', primary_key=True)
#     cve_periodo = models.IntegerField(blank=True, null=True)
#     numero_periodo = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'periodo_proyecto_empresa'
#         unique_together = (('cve_proyecto_empresa', 'numero_periodo'),)


# class PeriodoSolicitudBeca(models.Model):
#     cve_periodo_beca = models.SmallIntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='cve_periodo', blank=True, null=True)
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'periodo_solicitud_beca'


# class PeriodoSolicitudProrroga(models.Model):
#     cve_periodo_solicitud = models.IntegerField(primary_key=True)
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     monto_autorizado = models.DecimalField(max_digits=10, decimal_places=4)

#     class Meta:
#         managed = False
#         db_table = 'periodo_solicitud_prorroga'


# class Permiso(models.Model):
#     cve_permiso = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     cve_nomiplus = models.CharField(max_length=10, blank=True, null=True)
#     activo = models.BooleanField()
#     tipo = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'permiso'


# class PermisoCapturaComprobacion(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10)
#     cve_oficio = models.IntegerField()
#     fecha_permiso = models.DateTimeField()
#     fecha_registro = models.DateTimeField()
#     cve_empleado_registro = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'permiso_captura_comprobacion'


# class PermisoRegistrarProyecto(models.Model):
#     cve_permiso = models.IntegerField(primary_key=True)
#     cve_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='cve_persona')
#     cve_grupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='cve_grupo')
#     cve_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='cve_periodo')
#     fecha_permiso = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'permiso_registrar_proyecto'


# class PermissionRole(models.Model):
#     permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
#     role = models.ForeignKey('Roles', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'permission_role'
#         unique_together = (('permission', 'role'),)


# class PermissionUser(models.Model):
#     permission = models.ForeignKey('Permissions', models.DO_NOTHING)
#     user_id = models.BigIntegerField(primary_key=True)
#     user_type = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'permission_user'
#         unique_together = (('user_id', 'permission', 'user_type'),)


# class Permissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=255)
#     display_name = models.CharField(max_length=255, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'permissions'


# class Persona(models.Model):
#     cve_persona = models.IntegerField(primary_key=True)
#     cve_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='cve_pais')
#     cve_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='cve_ciudad')
#     cve_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='cve_estado_civil')
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=40, blank=True, null=True)
#     mail = models.CharField(max_length=60, blank=True, null=True)
#     movil = models.CharField(max_length=20, blank=True, null=True)
#     rfc = models.CharField(max_length=15)
#     curp = models.CharField(max_length=18, blank=True, null=True)
#     sexo = models.CharField(max_length=1)
#     fecha_nacimiento = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'persona'


# class PersonaCurriculum(models.Model):
#     cve_persona = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=70)
#     apellido_paterno = models.CharField(max_length=70)
#     apellido_materno = models.CharField(max_length=70)
#     mail = models.CharField(max_length=60)
#     movil = models.CharField(max_length=20)
#     rfc = models.CharField(max_length=15)
#     curp = models.CharField(max_length=19)
#     sexo = models.CharField(max_length=1)
#     fecha_nacimiento = models.DateTimeField()
#     cve_nacionalidad = models.IntegerField()
#     cve_ciudad = models.IntegerField()
#     cve_persona_interna = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'persona_curriculum'


# class PersonaEncuesta(models.Model):
#     cve_encuesta = models.ForeignKey(Encuesta, models.DO_NOTHING, db_column='cve_encuesta', blank=True, null=True)
#     tipo_persona = models.CharField(max_length=2)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'persona_encuesta'


# class PersonalAccessTokens(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     tokenable_type = models.CharField(max_length=255)
#     tokenable_id = models.BigIntegerField()
#     name = models.CharField(max_length=255)
#     token = models.CharField(unique=True, max_length=64)
#     abilities = models.TextField(blank=True, null=True)
#     last_used_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'personal_access_tokens'


# class PlanEstudio(models.Model):
#     cve_plan_estudio = models.SmallIntegerField(primary_key=True)
#     cve_carrera = models.ForeignKey(EspecialidadCarrera, models.DO_NOTHING, db_column='cve_carrera')
#     cve_especialidad = models.ForeignKey(EspecialidadCarrera, models.DO_NOTHING, db_column='cve_especialidad')
#     nombre = models.CharField(max_length=15)
#     fecha_inicio = models.DateTimeField()
#     tipo = models.CharField(max_length=1)
#     nomenclatura = models.CharField(max_length=5)
#     activo = models.BooleanField(blank=True, null=True)
#     punto_de_pase = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'plan_estudio'
#         unique_together = (('cve_plan_estudio', 'cve_carrera', 'cve_especialidad'),)


# class Plantel(models.Model):
#     cve_plantel = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     abreviatura = models.CharField(max_length=10, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'plantel'


# class PlantelUnidadAcademica(models.Model):
#     cve_plantel = models.ForeignKey(Plantel, models.DO_NOTHING, db_column='cve_plantel', blank=True, null=True)
#     cve_unidad_academica = models.ForeignKey('UnidadAcademica', models.DO_NOTHING, db_column='cve_unidad_academica', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'plantel_unidad_academica'


# class Pregunta(models.Model):
#     cve_pregunta = models.IntegerField(primary_key=True)
#     pregunta = models.CharField(max_length=255)
#     tipo_pregunta = models.SmallIntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'pregunta'


# class PreguntaEncuesta(models.Model):
#     cve_encuesta = models.OneToOneField(Encuesta, models.DO_NOTHING, db_column='cve_encuesta', primary_key=True)
#     cve_pregunta = models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='cve_pregunta')

#     class Meta:
#         managed = False
#         db_table = 'pregunta_encuesta'
#         unique_together = (('cve_encuesta', 'cve_pregunta'),)


# class PreguntaRespuesta(models.Model):
#     cve_respuesta = models.ForeignKey('Respuesta', models.DO_NOTHING, db_column='cve_respuesta')
#     cve_pregunta = models.ForeignKey('Respuesta', models.DO_NOTHING, db_column='cve_pregunta')
#     cve_encuestado = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pregunta_respuesta'


# class PreguntaRespuestaAbierta(models.Model):
#     cve_respuesta = models.IntegerField()
#     cve_pregunta = models.IntegerField()
#     cve_encuestado = models.IntegerField(blank=True, null=True)
#     comentario = models.CharField(max_length=600)

#     class Meta:
#         managed = False
#         db_table = 'pregunta_respuesta_abierta'


# class PreguntaRespuestaEncuestado(models.Model):
#     cve_respuesta = models.IntegerField()
#     cve_encuesta = models.OneToOneField(EncuestaConfiguracion, models.DO_NOTHING, db_column='cve_encuesta', primary_key=True)
#     cve_tipo_pregunta = models.ForeignKey('TipoPregunta', models.DO_NOTHING, db_column='cve_tipo_pregunta')
#     cve_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='cve_persona')
#     cve_grupo_seguridad = models.ForeignKey(GrupoSeguridad, models.DO_NOTHING, db_column='cve_grupo_seguridad')
#     cve_unidad_academica = models.IntegerField()
#     cve_periodo = models.SmallIntegerField()
#     cve_encuestado = models.IntegerField()
#     fecha_registro = models.DateTimeField()
#     comentario = models.CharField(max_length=450)
#     tipo_respuesta = models.IntegerField()
#     empresa = models.BooleanField()
#     valor_combo = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pregunta_respuesta_encuestado'
#         unique_together = (('cve_encuesta', 'cve_persona', 'cve_grupo_seguridad', 'cve_unidad_academica', 'cve_periodo', 'cve_respuesta', 'cve_tipo_pregunta'),)


# class PreguntaRespuestaEvaluado(models.Model):
#     cve_encuestado = models.IntegerField(blank=True, null=True)
#     cve_respuesta = models.IntegerField(blank=True, null=True)
#     cve_pregunta = models.IntegerField(blank=True, null=True)
#     cve_evaluado = models.IntegerField()
#     fecha = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pregunta_respuesta_evaluado'


# class PreguntaRespuestaEvaluadoAbierta(models.Model):
#     cve_respuesta = models.IntegerField()
#     cve_pregunta = models.IntegerField()
#     cve_encuestado = models.IntegerField()
#     cve_evaluado = models.IntegerField()
#     fecha = models.DateTimeField()
#     comentario = models.CharField(max_length=600)

#     class Meta:
#         managed = False
#         db_table = 'pregunta_respuesta_evaluado_abierta'


# class PreguntaRespuestaServicio(models.Model):
#     cve_respuesta = models.IntegerField(blank=True, null=True)
#     cve_pregunta = models.IntegerField(blank=True, null=True)
#     cve_encuestado = models.IntegerField(blank=True, null=True)
#     cve_servicio = models.IntegerField(blank=True, null=True)
#     cve_modulo = models.IntegerField(blank=True, null=True)
#     comentario = models.CharField(max_length=500, blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pregunta_respuesta_servicio'


# class PreguntaRespuestaVacante(models.Model):
#     cve_encuestado = models.IntegerField(blank=True, null=True)
#     cve_respuesta = models.IntegerField(blank=True, null=True)
#     cve_pregunta = models.IntegerField(blank=True, null=True)
#     fecha = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'pregunta_respuesta_vacante'


# class PrestamoIsseg(models.Model):
#     cve_prestamo = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     cve_tipo_prestamo = models.IntegerField(blank=True, null=True)
#     importe = models.FloatField()
#     numero_pagos = models.IntegerField()
#     descuento = models.FloatField()
#     fecha_inicio = models.DateTimeField()
#     fecha_termino = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'prestamo_isseg'


# class PrioridadServicio(models.Model):
#     cve_prioridad_servicio = models.IntegerField(primary_key=True)
#     cve_modulo = models.ForeignKey(ModuloServicio, models.DO_NOTHING, db_column='cve_modulo', blank=True, null=True)
#     nombre = models.CharField(max_length=100)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'prioridad_servicio'


# class Proceso(models.Model):
#     cve_proceso = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'proceso'


# class ProcesoCambioCuatrimestre(models.Model):
#     id_proceso_cambio_cuatrimestre = models.IntegerField(primary_key=True)
#     cve_usuario = models.IntegerField()
#     periodo = models.BooleanField(blank=True, null=True)
#     estatus = models.BooleanField(blank=True, null=True)
#     reinscripcion = models.BooleanField(blank=True, null=True)
#     estatus2 = models.BooleanField(blank=True, null=True)
#     subir_pagos = models.BooleanField(blank=True, null=True)
#     asignar_grupos_reinscritos = models.BooleanField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'proceso_cambio_cuatrimestre'


# class ProcesoFirmasCompras(models.Model):
#     cve_firma = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)
#     letra = models.CharField(max_length=1)
#     cve_tipo_persona = models.IntegerField()
#     orden = models.IntegerField()
#     entrada = models.IntegerField()
#     salida = models.IntegerField()
#     visibles = models.CharField(max_length=30)
#     extraordinario = models.BooleanField()
#     activo = models.BooleanField()
#     presupuesto = models.BooleanField()
#     partida = models.TextField()  # This field type is a guess.
#     area_academica = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'proceso_firmas_compras'


# class ProcesosRevalidacion(models.Model):
#     cve_proceso = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=100)
#     catalogo = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'procesos_revalidacion'


# class ProduccionDisenio(models.Model):
#     cve_solicitud = models.IntegerField()
#     presupuesto = models.FloatField(blank=True, null=True)
#     fecha_limite = models.DateTimeField(blank=True, null=True)
#     fecha_entrega_real = models.DateTimeField(blank=True, null=True)
#     horas_invertidas = models.FloatField(blank=True, null=True)
#     cve_diseniador = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'produccion_disenio'


# class ProgramacionExamen(models.Model):
#     cve_clase = models.OneToOneField(Clase, models.DO_NOTHING, db_column='cve_clase', primary_key=True)
#     cve_docente = models.ForeignKey(Clase, models.DO_NOTHING, db_column='cve_docente')
#     no_examen = models.SmallIntegerField()
#     fecha = models.DateTimeField()
#     tipo = models.CharField(max_length=2)
#     evaluador = models.CharField(max_length=10, blank=True, null=True)
#     fecha_limite = models.DateTimeField(blank=True, null=True)
#     cve_materia = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     no_unidad = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'programacion_examen'
#         unique_together = (('cve_clase', 'cve_docente', 'no_examen', 'no_unidad'),)


# class Promotor(models.Model):
#     cve_promotor = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=40, blank=True, null=True)
#     telefono = models.CharField(max_length=15)
#     email = models.CharField(max_length=60)
#     institucion = models.CharField(max_length=60)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'promotor'


# class PromotorCaptacion(models.Model):
#     cve_promotor = models.IntegerField()
#     cve_persona = models.IntegerField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'promotor_captacion'


# class Pronssss(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'pronssss'


# class Prorroga(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_periodo_solicitud = models.IntegerField()
#     cve_periodo = models.SmallIntegerField()
#     fecha_autorizacion = models.DateTimeField()
#     fecha_limite_pago = models.DateTimeField()
#     status = models.CharField(max_length=1)

#     class Meta:
#         managed = False
#         db_table = 'prorroga'
#         unique_together = (('matricula', 'cve_periodo_solicitud', 'cve_periodo'),)


# class Prospecto(models.Model):
#     cve_prospecto = models.IntegerField()
#     cve_bachillerato = models.IntegerField(blank=True, null=True)
#     cve_unidad_academica = models.IntegerField(blank=True, null=True)
#     cve_periodo = models.SmallIntegerField(blank=True, null=True)
#     cve_especialidad = models.SmallIntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=50, blank=True, null=True)
#     lada = models.CharField(max_length=50, blank=True, null=True)
#     telefono = models.CharField(max_length=50, blank=True, null=True)
#     celular = models.CharField(max_length=50, blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     opcion_carrera_uno = models.IntegerField(blank=True, null=True)
#     opcion_carrera_dos = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'prospecto'


# class ProspectoCorreo(models.Model):
#     cve_prospecto_correo = models.IntegerField()
#     cve_prospecto = models.IntegerField(blank=True, null=True)
#     cve_status_correo = models.IntegerField(blank=True, null=True)
#     numero_correo = models.IntegerField(blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'prospecto_correo'


# class ProspectoLlamada(models.Model):
#     cve_prospecto_llamada = models.IntegerField()
#     cve_prospecto = models.IntegerField(blank=True, null=True)
#     cve_status_llamada = models.IntegerField(blank=True, null=True)
#     intento = models.IntegerField(blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'prospecto_llamada'


# class Proveedor(models.Model):
#     cve_proveedor = models.IntegerField(primary_key=True)
#     cve_tipo = models.IntegerField(blank=True, null=True)
#     nombre_corto = models.CharField(max_length=200)
#     nombre = models.CharField(max_length=200)
#     rfc = models.CharField(max_length=20)
#     clave_patron = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'proveedor'


# class ProyectoEmpresaAlumno(models.Model):
#     cve_proyecto_empresa = models.OneToOneField('ProyectoEstadiaEmpresa', models.DO_NOTHING, db_column='cve_proyecto_empresa', primary_key=True)
#     cve_proyecto = models.IntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     fecha_actualizacion = models.DateTimeField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'proyecto_empresa_alumno'
#         unique_together = (('cve_proyecto_empresa', 'matricula'),)


# class ProyectoEstadia(models.Model):
#     cve_proyecto = models.IntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='cve_periodo')
#     matricula = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='matricula')
#     cve_empresa = models.ForeignKey(ContactoEmpresa, models.DO_NOTHING, db_column='cve_empresa')
#     cve_solicitante = models.ForeignKey(ContactoEmpresa, models.DO_NOTHING, db_column='cve_solicitante', blank=True, null=True)
#     cve_asesor_organizacional = models.SmallIntegerField(blank=True, null=True)
#     cve_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='cve_docente', blank=True, null=True)
#     cve_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='cve_departamento', blank=True, null=True)
#     area_trabajo = models.CharField(max_length=500)
#     proyecto_propuesto = models.CharField(max_length=500)
#     problema_resolver = models.CharField(max_length=500)
#     tipo = models.CharField(max_length=2)
#     observaciones = models.CharField(max_length=600, blank=True, null=True)
#     estado = models.CharField(max_length=2)
#     extension = models.CharField(max_length=4, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'proyecto_estadia'
#         unique_together = (('cve_proyecto', 'matricula', 'cve_periodo'),)


# class ProyectoEstadiaEmpresa(models.Model):
#     cve_proyecto_empresa = models.IntegerField(primary_key=True)
#     cve_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='cve_empresa', blank=True, null=True)
#     cve_solicitante = models.ForeignKey(ContactoEmpresa, models.DO_NOTHING, db_column='cve_solicitante', blank=True, null=True)
#     cve_asesor_organizacional = models.ForeignKey(ContactoEmpresa, models.DO_NOTHING, db_column='cve_asesor_organizacional', blank=True, null=True)
#     area_trabajo = models.CharField(max_length=500, blank=True, null=True)
#     proyecto_propuesto = models.CharField(max_length=500, blank=True, null=True)
#     problema_resolver = models.CharField(max_length=500, blank=True, null=True)
#     observaciones = models.CharField(max_length=600, blank=True, null=True)
#     numero_alumnos = models.IntegerField(blank=True, null=True)
#     numero_alumnos_real = models.IntegerField(blank=True, null=True)
#     estado = models.CharField(max_length=3, blank=True, null=True)
#     acceso = models.BooleanField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     fecha_actualizacion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'proyecto_estadia_empresa'


# class Prueba(models.Model):
#     cve = models.IntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'prueba'


# class Pruebabb(models.Model):
#     cve_prueba = models.IntegerField()
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pruebaBB'


# class Puesto(models.Model):
#     cve_puesto = models.IntegerField(primary_key=True)
#     cve_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='cve_departamento')
#     cve_tipo_puesto = models.ForeignKey('TipoPuesto', models.DO_NOTHING, db_column='cve_tipo_puesto')
#     cve_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='cve_empleado')
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField(blank=True, null=True)
#     nombre = models.CharField(max_length=100)
#     cve_centro_gestor = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'puesto'


# class PuestoBachillerato(models.Model):
#     cve_puesto = models.IntegerField()
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'puesto_bachillerato'


# class PuestoEgresado(models.Model):
#     cve_puesto_egresado = models.IntegerField(primary_key=True)
#     matricula = models.CharField(max_length=12)
#     cve_empresa = models.IntegerField()
#     cve_nivel_jerarquico = models.IntegerField(blank=True, null=True)
#     fecha_ingreso = models.DateTimeField(blank=True, null=True)
#     fecha_termino = models.DateTimeField(blank=True, null=True)
#     area_desempeno = models.CharField(max_length=60, blank=True, null=True)
#     puesto = models.CharField(max_length=60, blank=True, null=True)
#     actividad = models.CharField(max_length=260, blank=True, null=True)
#     sueldo_mensual = models.FloatField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'puesto_egresado'
#         unique_together = (('cve_puesto_egresado', 'matricula', 'cve_empresa'),)


# class PuestoInstitucion(models.Model):
#     cve_puesto = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=200)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'puesto_institucion'


# class PuntosAlumno(models.Model):
#     activo = models.BooleanField()
#     ano = models.CharField(max_length=4, blank=True, null=True)
#     beca = models.BooleanField()
#     car_alu = models.CharField(max_length=3, blank=True, null=True)
#     cua_asing = models.CharField(max_length=5, blank=True, null=True)
#     grupo_asing = models.CharField(max_length=5, blank=True, null=True)
#     id_beca = models.CharField(max_length=6, blank=True, null=True)
#     mat_alu = models.CharField(max_length=9, blank=True, null=True)
#     periodo = models.CharField(max_length=1, blank=True, null=True)
#     puntos = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'puntos_alumno'


# class Rango(models.Model):
#     cve_rango = models.IntegerField(primary_key=True)
#     cve_puesto = models.IntegerField()
#     cve_institucion = models.ForeignKey(Institucion, models.DO_NOTHING, db_column='cve_institucion')
#     rango = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'rango'


# class ReactivacionSolicitudServicio(models.Model):
#     cve_solicitud_servicio = models.ForeignKey('SolicitudServicio', models.DO_NOTHING, db_column='cve_solicitud_servicio', blank=True, null=True)
#     ultima_fecha_fin = models.DateTimeField(blank=True, null=True)
#     nueva_fecha_inicio = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'reactivacion_solicitud_servicio'


# class Rechazados(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'rechazados'


# class Recibo(models.Model):
#     cve_recibo = models.IntegerField(primary_key=True)
#     cve_unidad_academica = models.IntegerField()
#     cve_transaccion = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=1)
#     observaciones = models.CharField(max_length=300, blank=True, null=True)
#     fecha = models.DateTimeField()
#     folio = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'recibo'
#         unique_together = (('cve_recibo', 'cve_unidad_academica'),)


# class ReciboDonativo(models.Model):
#     cve_recibo_donativo = models.IntegerField(primary_key=True)
#     cve_transaccion = models.ForeignKey('Transaccion', models.DO_NOTHING, db_column='cve_transaccion', blank=True, null=True)
#     fecha = models.DateTimeField()
#     observaciones = models.CharField(max_length=100, blank=True, null=True)
#     status = models.CharField(max_length=1)
#     clave_memo = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'recibo_donativo'


# class RecursoOficio(models.Model):
#     cve_oficio = models.OneToOneField('self', models.DO_NOTHING, db_column='cve_oficio', primary_key=True)
#     valor_recurso = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'recurso_oficio'


# class ReferenciaPersonal(models.Model):
#     cve_referencia_personal = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField()
#     cve_parentesco = models.IntegerField()
#     cve_colonia = models.IntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=40, blank=True, null=True)
#     direccion = models.CharField(max_length=100, blank=True, null=True)
#     telefono = models.CharField(max_length=23, blank=True, null=True)
#     tutor = models.BooleanField()
#     tipo_referencia = models.CharField(max_length=1)
#     escolaridad = models.CharField(max_length=20, blank=True, null=True)
#     ocupacion = models.CharField(max_length=50, blank=True, null=True)
#     fecha_nacimiento = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'referencia_personal'
#         unique_together = (('cve_referencia_personal', 'cve_persona'),)


# class Referencias(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=8000)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=8000)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=8000)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=8000)  # Field name made lowercase.
#     col005 = models.CharField(db_column='Col005', max_length=8000)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'referencias'


class ReferenciasBanco(models.Model):
    cve_referencia = models.BigAutoField(primary_key=True)
    concepto = models.CharField(max_length=255, blank=True, null=True)
    matricula = models.CharField(max_length=255, blank=True, null=True)
    accion = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(unique=True, max_length=255, blank=True, null=True)
    banco_emisor = models.CharField(max_length=255, blank=True, null=True)
    servicio_bb = models.CharField(max_length=255, blank=True, null=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    forma_pago = models.CharField(max_length=255, blank=True, null=True)
    monto_parcial_minimo = models.DecimalField(max_digits=8, decimal_places=2)
    firma = models.TextField(blank=True, null=True)
    estatus = models.CharField(max_length=255, blank=True, null=True)
    mensaje = models.CharField(max_length=255, blank=True, null=True)
    monto_original = models.DecimalField(max_digits=8, decimal_places=2)
    recargo_aplicado = models.DecimalField(max_digits=8, decimal_places=2)
    descuento_aplicado = models.DecimalField(max_digits=8, decimal_places=2)
    monto_a_pagar = models.DecimalField(max_digits=8, decimal_places=2)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    no_recibo = models.CharField(max_length=255, blank=True, null=True)
    folio_pago = models.CharField(max_length=255, blank=True, null=True)
    fecha_limite_pago = models.CharField(max_length=10, blank=True, null=True)
    fecha_pago = models.DateField(max_length=10, blank=True, null=True)
    hora_pago = models.CharField(max_length=16, blank=True, null=True)
    folio_reverso = models.CharField(max_length=255, blank=True, null=True)
    fecha_reverso = models.CharField(max_length=10, blank=True, null=True)
    hora_reverso = models.CharField(max_length=16, blank=True, null=True)
    cve_periodo = models.ForeignKey(Periodo, on_delete=models.SET_NULL, blank=True, null=True, db_column='cve_periodo')
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    def get_unique_periodos(self):
        periodos = ReferenciasBanco.objects.values_list('cve_periodo', flat=True).distinct()
        return [(periodo, periodo.get_date_range()) for periodo in Periodo.objects.filter(cve_periodo__in=periodos)]

    class Meta:
        managed = False
        db_table = 'referencias_banco'

    def __str__(self):
        return self.concepto


# class ReferenciasBanco1(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     fecha = models.DateTimeField(blank=True, null=True)
#     matricula = models.CharField(max_length=255, blank=True, null=True)
#     referencia = models.CharField(max_length=255, blank=True, null=True)
#     monto = models.DecimalField(max_digits=8, decimal_places=2)
#     estatus = models.CharField(max_length=255, blank=True, null=True)
#     mensaje = models.CharField(max_length=255, blank=True, null=True)
#     accion = models.CharField(max_length=255, blank=True, null=True)
#     monto_original = models.DecimalField(max_digits=8, decimal_places=2)
#     recargo_aplicado = models.DecimalField(max_digits=8, decimal_places=2)
#     descuento_aplicado = models.DecimalField(max_digits=8, decimal_places=2)
#     monto_a_pagar = models.DecimalField(max_digits=8, decimal_places=2)
#     monto_parcial_minimo = models.DecimalField(max_digits=8, decimal_places=2)
#     nombre = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'referencias_banco1'


class ReferenciasConceptosBanco(models.Model):
    cve_concepto = models.BigAutoField(primary_key=True)
    num_concepto = models.CharField(max_length=255)
    concepto = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    monto_externo = models.DecimalField(max_digits=8, decimal_places=2)
    recargo = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_limite = models.BooleanField(help_text="Activar solo si se ingresa una fecha limite de pago.")
    fecha_limite_pago = models.DateField(max_length=10, blank=True, null=True)
    activo = models.BooleanField()
    cve_servicio = models.ForeignKey('ReferenciasServiciosBanco', models.DO_NOTHING, db_column='cve_servicio', blank=True, null=True)
    preferencial = models.BooleanField(help_text="Activar solo si el concepto tiene un monto preferencial")
    monto_preferencial = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'referencias_conceptos_banco'
        verbose_name = 'Concepto'
    
    def __str__(self):
        return self.concepto


# class ReferenciasMensajeConsultaBanco(models.Model):
#     cve_mensaje = models.BigAutoField(primary_key=True)
#     estatus = models.CharField(max_length=255, blank=True, null=True)
#     mensaje = models.CharField(max_length=255, blank=True, null=True)
#     fecha_creacion = models.DateTimeField()
#     fecha_actualizacion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'referencias_mensaje_consulta_banco'


class ReferenciasServiciosBanco(models.Model):
    cve_servicio = models.BigAutoField(primary_key=True)
    num_servicio = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'referencias_servicios_banco'
    
    def __str__(self):
        return self.num_servicio


# class RegistroCambioCalificacion(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     matricula = models.CharField(max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     no_parcial = models.SmallIntegerField()
#     cve_criterio = models.IntegerField()
#     calificacion_anterior = models.FloatField()
#     calificacion_actual = models.FloatField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'registro_cambio_calificacion'


# class RegistroJanium(models.Model):
#     cve_registro = models.IntegerField(primary_key=True)
#     cve_persona = models.IntegerField(blank=True, null=True)
#     tipo = models.CharField(max_length=20, blank=True, null=True)
#     cve_periodo = models.IntegerField(blank=True, null=True)
#     numero_cuenta = models.CharField(max_length=20, blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'registro_janium'


# class RegistroSesion(models.Model):
#     cve_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='cve_persona')
#     sesion = models.CharField(max_length=75)
#     proceso = models.BooleanField()
#     fecha = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'registro_sesion'


# class ReporteCuatrimestralTutoreo(models.Model):
#     cve_grupo = models.IntegerField()
#     cve_tutor = models.CharField(max_length=10)
#     situacion_grupo = models.CharField(max_length=3000, blank=True, null=True)
#     acuerdos_maestro = models.CharField(max_length=3000, blank=True, null=True)
#     logros_actividad = models.CharField(max_length=3000, blank=True, null=True)
#     obstaculos_actividad = models.CharField(max_length=3000, blank=True, null=True)
#     retos_personales = models.CharField(max_length=3000, blank=True, null=True)
#     sugerencias_institucion = models.CharField(max_length=3000, blank=True, null=True)
#     sugerencias_coordinador = models.CharField(max_length=3000, blank=True, null=True)
#     temas_sugeridos = models.CharField(max_length=3000, blank=True, null=True)
#     autoevaluacion = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'reporte_cuatrimestral_tutoreo'


# class ReporteMaestro(models.Model):
#     cve_reporte = models.IntegerField(primary_key=True)
#     cve_concepto = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'reporte_maestro'


# class Requisicion(models.Model):
#     cve_requisicion = models.IntegerField(primary_key=True)
#     folio = models.IntegerField()
#     cve_departamento = models.SmallIntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     motivo = models.CharField(max_length=500)
#     fecha_registro = models.DateTimeField()
#     fecha_recepcion = models.DateTimeField()
#     status = models.CharField(max_length=2)
#     activo = models.BooleanField()
#     extraordinario = models.BooleanField()
#     costo_estimado = models.FloatField()
#     recurso_comprometido = models.CharField(max_length=10, blank=True, null=True)
#     tipo_recurso = models.CharField(max_length=20, blank=True, null=True)
#     fecha_revision = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'requisicion'


# class RequisicionArticulo(models.Model):
#     cve_requisicion = models.IntegerField(primary_key=True)
#     cve_articulo = models.IntegerField()
#     cve_articulo_requisicion = models.IntegerField()
#     cve_unidad_medida = models.SmallIntegerField()
#     cantidad = models.IntegerField()
#     descripcion = models.CharField(max_length=500)
#     fecha = models.DateTimeField()
#     status = models.CharField(max_length=2)
#     activo = models.BooleanField()
#     centro_costo_alterno = models.CharField(max_length=5, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'requisicion_articulo'
#         unique_together = (('cve_requisicion', 'cve_articulo'),)


# class RequisicionArticuloCancelar(models.Model):
#     cve_requisicion = models.IntegerField()
#     cve_articulo = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     motivo = models.CharField(max_length=100)
#     fecha = models.DateTimeField()
#     status_anterior = models.CharField(max_length=2)
#     especial = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'requisicion_articulo_cancelar'


# class RequisicionArticuloHistorial(models.Model):
#     cve_historial = models.IntegerField(primary_key=True)
#     cve_revision = models.SmallIntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     cve_requisicion = models.IntegerField()
#     cve_articulo = models.IntegerField()
#     fecha = models.DateTimeField()
#     status_anterior = models.CharField(max_length=2)
#     observacion = models.CharField(max_length=200)

#     class Meta:
#         managed = False
#         db_table = 'requisicion_articulo_historial'


# class RequisicionArticuloRecepcion(models.Model):
#     cve_recepcion = models.IntegerField(primary_key=True)
#     cve_agrupacion = models.IntegerField()
#     cve_cotizacion = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha = models.DateTimeField()
#     status = models.CharField(max_length=1, blank=True, null=True)
#     observaciones = models.CharField(max_length=50, blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     status_orden = models.CharField(max_length=1, blank=True, null=True)
#     folio_recepcion = models.CharField(max_length=50, blank=True, null=True)
#     calificacion_proveedor = models.IntegerField(blank=True, null=True)
#     fecha_requisicion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'requisicion_articulo_recepcion'


# class RequisicionCancelar(models.Model):
#     cve_requisicion = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     motivo = models.CharField(max_length=200)
#     fecha = models.DateTimeField()
#     status_anterior = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'requisicion_cancelar'


# class RequisicionHorario(models.Model):
#     cve_requisicion_horario = models.IntegerField()
#     dia_semana = models.IntegerField()
#     hora_inicio = models.CharField(max_length=10)
#     hora_fin = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'requisicion_horario'


# class RequisicionProveedor(models.Model):
#     cve_requisicion = models.IntegerField()
#     cve_proveedor = models.IntegerField()
#     motivo = models.CharField(max_length=200)
#     fecha = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'requisicion_proveedor'


# class Requisito(models.Model):
#     cve_requisito = models.IntegerField(primary_key=True)
#     cve_beca = models.ForeignKey(Beca, models.DO_NOTHING, db_column='cve_beca')
#     promedio_minimo = models.IntegerField()
#     cuatrimestre_min_presurizado = models.IntegerField()
#     cuatrimestre_max_presurizado = models.IntegerField()
#     cuatrimestre_min_despresurizado = models.IntegerField()
#     cuatrimestre_max_despresurizado = models.IntegerField()
#     status_materias = models.IntegerField()
#     ingresos_maximos = models.FloatField()
#     cve_unidad_academica = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'requisito'
#         unique_together = (('cve_requisito', 'cve_beca'),)


# class ResponsableServicio(models.Model):
#     cve_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='cve_persona', blank=True, null=True)
#     cve_departamento = models.ForeignKey('ServicioPorDepartamento', models.DO_NOTHING, db_column='cve_departamento', blank=True, null=True)
#     cve_servicio = models.ForeignKey('ServicioPorDepartamento', models.DO_NOTHING, db_column='cve_servicio', blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'responsable_servicio'


# class Respuesta(models.Model):
#     cve_respuesta = models.IntegerField(primary_key=True)
#     cve_pregunta = models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='cve_pregunta')
#     respuesta = models.CharField(max_length=255)
#     abierta = models.BooleanField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'respuesta'
#         unique_together = (('cve_respuesta', 'cve_pregunta'),)


# class Restriccion(models.Model):
#     cve_restriccion = models.IntegerField(primary_key=True)
#     restriccion = models.CharField(max_length=100)
#     datos = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'restriccion'


# class RestriccionConcepto(models.Model):
#     cve_restriccion = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=350)
#     fecha_limite = models.DateTimeField()
#     cve_periodo = models.IntegerField()
#     mes = models.IntegerField()
#     numero_parcial = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'restriccion_concepto'


# class RestriccionConceptoCarrera(models.Model):
#     cve_restriccion = models.IntegerField(primary_key=True)
#     cve_especialidad = models.IntegerField()
#     cve_carrera = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     cve_plan_estudio = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'restriccion_concepto_carrera'
#         unique_together = (('cve_restriccion', 'cve_especialidad', 'cve_carrera', 'cve_periodo', 'cve_plan_estudio'),)


# class RestriccionConceptoIndice(models.Model):
#     cve_concepto = models.IntegerField(primary_key=True)
#     cve_restriccion = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'restriccion_concepto_indice'
#         unique_together = (('cve_concepto', 'cve_restriccion'),)


# class RestriccionPorPermiso(models.Model):
#     cve_restriccion_permiso = models.IntegerField(primary_key=True)
#     cve_permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='cve_permiso')
#     cve_restriccion = models.ForeignKey(Restriccion, models.DO_NOTHING, db_column='cve_restriccion')
#     valor = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'restriccion_por_permiso'
#         unique_together = (('cve_restriccion_permiso', 'cve_permiso', 'cve_restriccion'),)


# class ResultadoBeca(models.Model):
#     cve_convocatoria = models.OneToOneField('ValidacionBeca', models.DO_NOTHING, db_column='cve_convocatoria', primary_key=True)
#     matricula = models.ForeignKey('ValidacionBeca', models.DO_NOTHING, db_column='matricula')
#     resultado = models.BooleanField()
#     observaciones = models.CharField(max_length=1000)
#     fecha_registro = models.DateTimeField()
#     monto_otorgado = models.FloatField()
#     cve_sesion = models.ForeignKey('SesionComite', models.DO_NOTHING, db_column='cve_sesion')

#     class Meta:
#         managed = False
#         db_table = 'resultado_beca'
#         unique_together = (('cve_convocatoria', 'matricula'),)


# class ResultadoCeneval(models.Model):
#     folio_ceneval = models.CharField(primary_key=True, max_length=10)
#     cve_aspirante = models.IntegerField()
#     promedio = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'resultado_ceneval'


# class Retroalimentacion(models.Model):
#     cve_retroalimentacion = models.IntegerField(primary_key=True)
#     cve_departamento = models.ForeignKey('ServicioPorDepartamento', models.DO_NOTHING, db_column='cve_departamento')
#     cve_servicio = models.ForeignKey('ServicioPorDepartamento', models.DO_NOTHING, db_column='cve_servicio')
#     cve_tipo_retroalimentacion = models.ForeignKey('TipoRetroalimentacion', models.DO_NOTHING, db_column='cve_tipo_retroalimentacion', blank=True, null=True)
#     fecha_registro = models.DateTimeField()
#     fecha_incidente = models.DateTimeField()
#     asunto = models.CharField(max_length=50, blank=True, null=True)
#     comentario = models.CharField(max_length=3000, blank=True, null=True)
#     cve_persona = models.IntegerField()
#     status_atencion = models.SmallIntegerField(blank=True, null=True)
#     observaciones = models.CharField(max_length=400, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'retroalimentacion'


# class Revalidacion(models.Model):
#     folio_revalidadacion = models.IntegerField(primary_key=True)
#     matricula = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='matricula')
#     cve_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='cve_docente')
#     fecha = models.DateTimeField()
#     calificacion = models.IntegerField()
#     status = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'revalidacion'


# class Revaloracion(models.Model):
#     cve_solicitud = models.ForeignKey(DatosMedicosPermiso, models.DO_NOTHING, db_column='cve_solicitud', blank=True, null=True)
#     cve_empleado = models.ForeignKey(DatosMedicosPermiso, models.DO_NOTHING, db_column='cve_empleado', blank=True, null=True)
#     folio = models.ForeignKey(DatosMedicosPermiso, models.DO_NOTHING, db_column='folio', blank=True, null=True)
#     fecha_revaloracion = models.DateTimeField(blank=True, null=True)
#     status = models.CharField(max_length=3, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'revaloracion'


# class RoleUser(models.Model):
#     role = models.ForeignKey('Roles', models.DO_NOTHING)
#     user_id = models.BigIntegerField(primary_key=True)
#     user_type = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'role_user'
#         unique_together = (('user_id', 'role', 'user_type'),)


# class Roles(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=255)
#     display_name = models.CharField(max_length=255, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'roles'


# class RubroCalificacionEmpresa(models.Model):
#     cve_rubro_calificacion = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     valor = models.IntegerField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'rubro_calificacion_empresa'


# class SecretarioAcademico(models.Model):
#     cve_unidad_academica = models.SmallIntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'secretario_academico'


# class Sector(models.Model):
#     cve_sector = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'sector'


# class SeguimientoAlumnoTutoreo(models.Model):
#     cve_seguimiento_alumno = models.IntegerField()
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     cve_seguimiento_grupal = models.IntegerField(blank=True, null=True)
#     asistio = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'seguimiento_alumno_tutoreo'


# class SeguimientoEstadia(models.Model):
#     cve_proyecto = models.IntegerField()
#     cve_periodo = models.SmallIntegerField(primary_key=True)
#     matricula = models.CharField(max_length=12)
#     fip = models.BooleanField(blank=True, null=True)
#     entrega_convenio = models.BooleanField(blank=True, null=True)
#     categoria = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'seguimiento_estadia'
#         unique_together = (('cve_periodo', 'matricula'),)


# class SeguimientoEstadiaComentario(models.Model):
#     cve_comentario_seguimiento = models.IntegerField(primary_key=True)
#     cve_periodo = models.ForeignKey(SeguimientoEstadia, models.DO_NOTHING, db_column='cve_periodo')
#     matricula = models.ForeignKey(SeguimientoEstadia, models.DO_NOTHING, db_column='matricula')
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     comentario = models.CharField(max_length=500, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'seguimiento_estadia_comentario'


# class SeguimientoEstatus(models.Model):
#     cve_solicitud_servicio = models.ForeignKey('SolicitudServicio', models.DO_NOTHING, db_column='cve_solicitud_servicio', blank=True, null=True)
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     status_anterior = models.IntegerField(blank=True, null=True)
#     status_actual = models.IntegerField(blank=True, null=True)
#     comentarios = models.CharField(max_length=300, blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'seguimiento_estatus'


# class SeguimientoGrupalTutoreo(models.Model):
#     cve_seguimiento_grupal = models.IntegerField()
#     cve_grupo = models.IntegerField(blank=True, null=True)
#     cve_tutor = models.CharField(max_length=10, blank=True, null=True)
#     semana = models.SmallIntegerField(blank=True, null=True)
#     tema = models.CharField(max_length=255, blank=True, null=True)
#     fecha_sesion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'seguimiento_grupal_tutoreo'


# class ServicioBecario(models.Model):
#     cve_proyecto = models.IntegerField(primary_key=True)
#     cve_convocatoria = models.ForeignKey(ResultadoBeca, models.DO_NOTHING, db_column='cve_convocatoria')
#     matricula = models.ForeignKey(ResultadoBeca, models.DO_NOTHING, db_column='matricula')
#     cve_departamento = models.IntegerField()
#     lugar = models.CharField(max_length=50)
#     proyecto = models.CharField(max_length=1000)
#     status = models.CharField(max_length=1)
#     total_horas = models.IntegerField()
#     resultados = models.CharField(max_length=50)
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'servicio_becario'
#         unique_together = (('cve_proyecto', 'cve_convocatoria', 'matricula'),)


# class ServicioDisenio(models.Model):
#     cve_servicio = models.IntegerField()
#     cve_solicitud = models.IntegerField(blank=True, null=True)
#     cve_descripcion = models.IntegerField(blank=True, null=True)
#     descripcion = models.CharField(max_length=1000, blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#     produccion = models.IntegerField(blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'servicio_disenio'


# class ServicioLiberacion(models.Model):
#     cve_departamento = models.OneToOneField('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_departamento', primary_key=True)
#     cve_servicio = models.ForeignKey('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_servicio')
#     cve_especialidad = models.ForeignKey('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_especialidad')
#     cve_carrera = models.ForeignKey('ServiciosPorCarrera', models.DO_NOTHING, db_column='cve_carrera')
#     cve_proceso = models.SmallIntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'servicio_liberacion'
#         unique_together = (('cve_departamento', 'cve_servicio', 'cve_especialidad', 'cve_carrera', 'cve_proceso'),)


# class ServicioPorDepartamento(models.Model):
#     cve_departamento = models.OneToOneField(Departamento, models.DO_NOTHING, db_column='cve_departamento', primary_key=True)
#     cve_servicio = models.IntegerField()
#     servicio = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'servicio_por_departamento'
#         unique_together = (('cve_departamento', 'cve_servicio'),)


# class ServicioProcesoDocumento(models.Model):
#     cve_modulo = models.IntegerField()
#     cve_proceso = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'servicio_proceso_documento'


# class ServicioRetroalimentacionActivo(models.Model):
#     cve_departamento = models.OneToOneField(ServicioPorDepartamento, models.DO_NOTHING, db_column='cve_departamento', primary_key=True)
#     cve_servicio = models.ForeignKey(ServicioPorDepartamento, models.DO_NOTHING, db_column='cve_servicio')
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'servicio_retroalimentacion_activo'
#         unique_together = (('cve_departamento', 'cve_servicio'),)


# class ServiciosPorCarrera(models.Model):
#     cve_departamento = models.OneToOneField(ServicioPorDepartamento, models.DO_NOTHING, db_column='cve_departamento', primary_key=True)
#     cve_servicio = models.ForeignKey(ServicioPorDepartamento, models.DO_NOTHING, db_column='cve_servicio')
#     cve_especialidad = models.SmallIntegerField()
#     cve_carrera = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'servicios_por_carrera'
#         unique_together = (('cve_departamento', 'cve_servicio', 'cve_especialidad', 'cve_carrera'),)


# class SesionComite(models.Model):
#     cve_sesion = models.IntegerField(primary_key=True)
#     numero_sesion = models.IntegerField()
#     fecha_sesion = models.DateTimeField()
#     tipo_sesion = models.CharField(max_length=1)
#     asistentes = models.CharField(max_length=1000)

#     class Meta:
#         managed = False
#         db_table = 'sesion_comite'


# class SistemaBachillerato(models.Model):
#     cve_sistema_bachillerato = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=30)

#     class Meta:
#         managed = False
#         db_table = 'sistema_bachillerato'


# class SolicitudAdmision(models.Model):
#     cve_solicitud_admision = models.OneToOneField('self', models.DO_NOTHING, db_column='cve_solicitud_admision', primary_key=True)
#     cve_unidad_academica = models.SmallIntegerField()
#     cve_area_academica1 = models.SmallIntegerField()
#     cve_carrera1 = models.SmallIntegerField()
#     cve_area_academica2 = models.SmallIntegerField(blank=True, null=True)
#     cve_carrera2 = models.SmallIntegerField(blank=True, null=True)
#     cve_turno = models.CharField(max_length=1)
#     status = models.CharField(max_length=1)
#     referencia_pago = models.CharField(max_length=20)
#     cve_especialidad1 = models.SmallIntegerField(blank=True, null=True)
#     cve_especialidad2 = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_admision'


# class SolicitudAdmisionLic(models.Model):
#     cve_solicitud_admision = models.SmallIntegerField(primary_key=True)
#     cve_unidad_academica = models.SmallIntegerField()
#     cve_area_academica1 = models.SmallIntegerField()
#     cve_carrera1 = models.SmallIntegerField()
#     cve_especialidad1 = models.SmallIntegerField()
#     cve_turno = models.CharField(max_length=1)
#     status = models.CharField(max_length=1)
#     referencia_pago = models.CharField(max_length=20)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_admision_lic'


# class SolicitudAdmisionLicProf(models.Model):
#     cve_solicitud_admision = models.SmallIntegerField()
#     cve_unidad_academica = models.SmallIntegerField()
#     cve_area_academica1 = models.SmallIntegerField()
#     cve_carrera1 = models.SmallIntegerField()
#     cve_especialidad1 = models.SmallIntegerField()
#     turno = models.CharField(max_length=1)
#     status = models.CharField(max_length=1)
#     referencia_pago = models.CharField(max_length=20)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_admision_lic_prof'


# class SolicitudBaja(models.Model):
#     cve_persona_tramite = models.IntegerField()
#     cve_baja = models.IntegerField()
#     comentario = models.CharField(max_length=1000, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_baja'


# class SolicitudBeca(models.Model):
#     matricula = models.OneToOneField(Alumno, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_convocatoria = models.ForeignKey(Convocatoria, models.DO_NOTHING, db_column='cve_convocatoria')
#     tipo = models.CharField(max_length=1)
#     fecha_solicitud = models.DateTimeField()
#     documentos_entregados = models.CharField(max_length=50)
#     promedio = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'solicitud_beca'
#         unique_together = (('matricula', 'cve_convocatoria'),)


# class SolicitudBecaInscripcion(models.Model):
#     cve_solicitud_beca = models.IntegerField(primary_key=True)
#     cve_tipo_beca = models.ForeignKey('TipoBeca', models.DO_NOTHING, db_column='cve_tipo_beca')
#     cve_periodo_beca = models.IntegerField()
#     matricula = models.CharField(max_length=10)
#     tipo_solicitud = models.IntegerField()
#     cve_periodo = models.IntegerField()
#     fecha_solicitud = models.DateTimeField()
#     tiempo_traslado = models.IntegerField(blank=True, null=True)
#     medio_transporte = models.IntegerField(blank=True, null=True)
#     viaje_diario = models.BooleanField(blank=True, null=True)
#     domicilio_leon = models.CharField(max_length=100, blank=True, null=True)
#     beca_institucion = models.CharField(max_length=75, blank=True, null=True)
#     viven_padre = models.IntegerField(blank=True, null=True)
#     cve_estado_civil = models.IntegerField(blank=True, null=True)
#     ocupacion_padre = models.CharField(max_length=50, blank=True, null=True)
#     ocupacion_madre = models.CharField(max_length=50, blank=True, null=True)
#     dependencia_economica = models.CharField(max_length=50, blank=True, null=True)
#     finalidad_trabajo = models.IntegerField(blank=True, null=True)
#     frecuencia_cantidad = models.CharField(max_length=25, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_beca_inscripcion'


# class SolicitudBecaLeon(models.Model):
#     col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col002 = models.CharField(db_column='Col002', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col003 = models.CharField(db_column='Col003', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col004 = models.CharField(db_column='Col004', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col005 = models.CharField(db_column='Col005', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     col006 = models.CharField(db_column='Col006', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'solicitud_beca_leon'


# class SolicitudCambioCalificacion(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_solicitud = models.IntegerField()
#     cve_director = models.CharField(max_length=10)
#     fecha_cambio = models.DateTimeField()
#     cve_motivo = models.ForeignKey(MotivoCambioCalificacion, models.DO_NOTHING, db_column='cve_motivo')
#     numero_unidad = models.SmallIntegerField()
#     numero_oficio = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_cambio_calificacion'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_solicitud', 'cve_director'),)


# class SolicitudCambioCalificacionRecuperacion(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_solicitud = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     fecha_cambio = models.DateTimeField()
#     numero_oficio = models.CharField(max_length=10)
#     tipo = models.CharField(max_length=5, blank=True, null=True)
#     cve_motivo = models.ForeignKey(MotivoCambioCalificacion, models.DO_NOTHING, db_column='cve_motivo', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_cambio_calificacion_recuperacion'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_solicitud'),)


# class SolicitudCambioCalificacionRemedial(models.Model):
#     matricula = models.CharField(primary_key=True, max_length=12)
#     cve_clase = models.IntegerField()
#     cve_docente = models.CharField(max_length=10)
#     cve_solicitud = models.IntegerField()
#     cve_director = models.CharField(max_length=10)
#     fecha_cambio = models.DateTimeField()
#     cve_motivo = models.ForeignKey(MotivoCambioCalificacion, models.DO_NOTHING, db_column='cve_motivo', blank=True, null=True)
#     numero_oficio = models.CharField(max_length=10)
#     numero_unidad = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'solicitud_cambio_calificacion_remedial'
#         unique_together = (('matricula', 'cve_clase', 'cve_docente', 'cve_solicitud', 'numero_unidad'),)


# class SolicitudDisenio(models.Model):
#     cve_solicitud = models.IntegerField()
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     cve_area = models.IntegerField(blank=True, null=True)
#     folio = models.CharField(max_length=10, blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)
#     proyecto = models.CharField(max_length=50, blank=True, null=True)
#     objetivo = models.CharField(max_length=250, blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     nivel_importancia = models.IntegerField(blank=True, null=True)
#     observaciones = models.CharField(max_length=250, blank=True, null=True)
#     restricciones = models.CharField(max_length=250, blank=True, null=True)
#     encuesta_realizada = models.BooleanField(blank=True, null=True)
#     cve_encuestado = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_disenio'


# class SolicitudEmpleoConvocatoria(models.Model):
#     cve_solicitud_empleo = models.IntegerField()
#     cve_convocatoria = models.IntegerField()
#     seleccionado = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'solicitud_empleo_convocatoria'


# class SolicitudEmpleoDatosPersonales(models.Model):
#     cve_solicitud_empleo = models.IntegerField()
#     cve_ciudad = models.IntegerField()
#     cve_colonia = models.IntegerField()
#     cves_unidades_academicas = models.CharField(max_length=20)
#     nombre = models.CharField(max_length=100)
#     apellido_paterno = models.CharField(max_length=60)
#     apellido_materno = models.CharField(max_length=60)
#     direccion = models.CharField(max_length=200)
#     rfc = models.CharField(max_length=20)
#     curp = models.CharField(max_length=20)
#     telefono = models.CharField(max_length=20)
#     telefono_domicilio = models.CharField(max_length=20)
#     telefono_recados = models.CharField(max_length=20)
#     email = models.CharField(max_length=60)
#     lugar_nacimiento = models.CharField(max_length=100)
#     fecha_nacimiento = models.DateTimeField()
#     edad_cumplida = models.IntegerField()
#     estado_civil = models.IntegerField()
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     observaciones = models.CharField(max_length=1000, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_empleo_datos_personales'


# class SolicitudEmpleoEscolaridadBasicaSimple(models.Model):
#     cve_solicitud_empleo = models.IntegerField()
#     grado = models.CharField(max_length=50)
#     especialidad = models.CharField(max_length=50)
#     certificado = models.BooleanField()
#     titulo = models.BooleanField()
#     cedula = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'solicitud_empleo_escolaridad_basica_simple'


# class SolicitudEmpleoEscolaridadCatalogo(models.Model):
#     cve_escolaridad = models.IntegerField()
#     nombre = models.CharField(max_length=30)
#     activo = models.BooleanField()
#     especial = models.BooleanField()
#     orden = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_empleo_escolaridad_catalogo'


# class SolicitudEmpleoEscolaridadSuperiorSimple(models.Model):
#     cve_solicitud_empleo = models.IntegerField()
#     cve_escolaridad = models.IntegerField()
#     nombre_carrera = models.TextField()  # This field type is a guess.
#     rama_academica = models.TextField()  # This field type is a guess.
#     nombre_institucion = models.TextField()  # This field type is a guess.
#     certificado = models.BooleanField()
#     titulo = models.BooleanField()
#     cedula = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'solicitud_empleo_escolaridad_superior_simple'


# class SolicitudEmpleoEstudiosComplementarios(models.Model):
#     cve_solicitud_empleo = models.IntegerField()
#     cve_curso = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     fecha = models.CharField(max_length=100)
#     duracion = models.CharField(max_length=60)
#     instituto_impartido = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_empleo_estudios_complementarios'


# class SolicitudEmpleoExperienciaLaboralSimple(models.Model):
#     cve_solicitud_empleo = models.IntegerField()
#     cve_experiencia_laboral = models.IntegerField()
#     razon_social = models.CharField(max_length=150)
#     telefono = models.CharField(max_length=20)
#     personas_a_cargo = models.IntegerField()
#     sueldo_ultimo = models.IntegerField()
#     fecha_ingreso = models.CharField(max_length=50)
#     fecha_salida = models.CharField(max_length=50)
#     motivo_separacion = models.CharField(max_length=50)
#     puesto_final_ocupado = models.CharField(max_length=50)
#     tiempo_puesto_final = models.CharField(max_length=50)
#     puesto_anterior = models.CharField(max_length=50)
#     tiempo_puesto_anterior = models.CharField(max_length=50)
#     jefe_ultimo_puesto = models.CharField(max_length=50)
#     autorizar_referencias = models.BooleanField()
#     proyecto_estadia = models.CharField(max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_empleo_experiencia_laboral_simple'


# class SolicitudPermiso(models.Model):
#     cve_solicitud = models.IntegerField(primary_key=True)
#     cve_empleado = models.CharField(max_length=16)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     fecha_inicio = models.DateTimeField(blank=True, null=True)
#     fecha_fin = models.DateTimeField(blank=True, null=True)
#     folio = models.CharField(max_length=10)
#     cve_permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='cve_permiso', blank=True, null=True)
#     cve_motivo = models.IntegerField(blank=True, null=True)
#     fecha_intermedia = models.DateTimeField(blank=True, null=True)
#     status = models.CharField(max_length=2, blank=True, null=True)
#     observaciones = models.CharField(max_length=500, blank=True, null=True)
#     descuento = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_permiso'
#         unique_together = (('cve_solicitud', 'cve_empleado', 'folio'),)


# class SolicitudProrroga(models.Model):
#     matricula = models.OneToOneField(Alumno, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_periodo_solicitud = models.IntegerField()
#     cve_periodo = models.SmallIntegerField()
#     fecha_solicitud = models.DateTimeField()
#     cve_motivo = models.ForeignKey(MotivoProrroga, models.DO_NOTHING, db_column='cve_motivo')
#     comentarios = models.CharField(max_length=1000)
#     status = models.CharField(max_length=1)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_prorroga'
#         unique_together = (('matricula', 'cve_periodo_solicitud', 'cve_periodo'),)


# class SolicitudServicio(models.Model):
#     cve_solicitud_servicio = models.IntegerField(primary_key=True)
#     cve_modulo = models.ForeignKey(ModuloServicio, models.DO_NOTHING, db_column='cve_modulo')
#     folio = models.IntegerField(blank=True, null=True)
#     cve_departamento = models.IntegerField(blank=True, null=True)
#     cve_empleado = models.CharField(max_length=10, blank=True, null=True)
#     descripcion = models.CharField(max_length=500, blank=True, null=True)
#     cve_tipo_servicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='cve_tipo_servicio', blank=True, null=True)
#     cve_espacio = models.ForeignKey('UbicacionEspacio', models.DO_NOTHING, db_column='cve_espacio', blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     fecha_fin = models.DateTimeField(blank=True, null=True)
#     extraordinario = models.BooleanField(blank=True, null=True)
#     id_status = models.ForeignKey('StatusSeguimientoServicio', models.DO_NOTHING, db_column='id_status', blank=True, null=True)
#     cve_prioridad_servicio = models.ForeignKey(PrioridadServicio, models.DO_NOTHING, db_column='cve_prioridad_servicio', blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_servicio'


# class SolicitudTitulacion(models.Model):
#     folio = models.IntegerField()
#     cve_periodo = models.SmallIntegerField()
#     matricula = models.CharField(max_length=12)
#     fecha = models.DateTimeField()
#     recibo = models.CharField(max_length=15)

#     class Meta:
#         managed = False
#         db_table = 'solicitud_titulacion'


# class SolicitudTramiteServicio(models.Model):
#     cve_solicitud = models.IntegerField(primary_key=True)
#     cve_tramite = models.ForeignKey('TipoTramiteServicio', models.DO_NOTHING, db_column='cve_tramite')
#     matricula = models.CharField(max_length=12)
#     motivo = models.CharField(max_length=300)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'solicitud_tramite_servicio'


# class StatusAlumno(models.Model):
#     cve_status = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=2)
#     descripcion = models.CharField(max_length=50)
#     activo = models.BooleanField()
#     tipo = models.CharField(max_length=1)

#     class Meta:
#         managed = False
#         db_table = 'status_alumno'


# class StatusBeca(models.Model):
#     cve_solicitud_beca = models.IntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     status = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'status_beca'


# class StatusCalificacion(models.Model):
#     cve_status = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=20)
#     descripcion = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'status_calificacion'


# class StatusCorreoProspecto(models.Model):
#     cve_status_correo = models.IntegerField()
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'status_correo_prospecto'


# class StatusInvitado(models.Model):
#     cve_status_invitado = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'status_invitado'


# class StatusLlamada(models.Model):
#     cve_status_llamada = models.IntegerField()
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     tipo = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'status_llamada'


# class StatusPersonaFirmar(models.Model):
#     cve_empleado = models.CharField(max_length=10)
#     tipo_status = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'status_persona_firmar'


# class StatusSeguimiento(models.Model):
#     id_status = models.IntegerField(primary_key=True)
#     status = models.CharField(max_length=3)
#     descripcion = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'status_seguimiento'


# class StatusSeguimientoServicio(models.Model):
#     id_status = models.IntegerField(primary_key=True)
#     cve_modulo = models.ForeignKey(ModuloServicio, models.DO_NOTHING, db_column='cve_modulo')
#     descripcion = models.CharField(max_length=100, blank=True, null=True)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'status_seguimiento_servicio'


# class Subcapitulo(models.Model):
#     cve_subcapitulo = models.IntegerField(primary_key=True)
#     cve_capitulo = models.ForeignKey(Capitulo, models.DO_NOTHING, db_column='cve_capitulo')
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=800)
#     activo = models.BooleanField()
#     clave = models.CharField(max_length=4)
#     cve_naturaleza = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'subcapitulo'


# class SueldoEmpleado(models.Model):
#     cve_puesto = models.IntegerField(primary_key=True)
#     cve_departamento = models.SmallIntegerField()
#     cve_empleado = models.CharField(max_length=10)
#     cve_tipo_puesto = models.SmallIntegerField()
#     horas = models.IntegerField()
#     precio_hora = models.FloatField()
#     sueldo = models.FloatField()
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sueldo_empleado'


# class Sysdiagrams(models.Model):
#     name = models.CharField(max_length=128)
#     principal_id = models.IntegerField()
#     diagram_id = models.AutoField(primary_key=True)
#     version = models.IntegerField(blank=True, null=True)
#     definition = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sysdiagrams'
#         unique_together = (('principal_id', 'name'),)


# class Tablaprueba(models.Model):
#     colum1 = models.CharField(max_length=50, blank=True, null=True)
#     colum2 = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tablaprueba'


# class TabuladorLicencia(models.Model):
#     cve_tabulador = models.IntegerField(primary_key=True)
#     cve_permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='cve_permiso', blank=True, null=True)
#     minimo = models.IntegerField()
#     maximo = models.IntegerField()
#     dias = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tabulador_licencia'


# class Tamano(models.Model):
#     cve_tamano = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tamano'


# class TarifaValesGasolina(models.Model):
#     cve_tarifa = models.IntegerField()
#     cve_ciudad = models.IntegerField()
#     destino = models.CharField(max_length=100, blank=True, null=True)
#     km = models.IntegerField()
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tarifa_vales_gasolina'


# class TarifaVehiculo(models.Model):
#     cve_tipo_vehiculo = models.IntegerField()
#     cve_tarifa = models.IntegerField()
#     cantidad = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'tarifa_vehiculo'


# class TarifaViatico(models.Model):
#     cve_tarifa = models.IntegerField(primary_key=True)
#     cve_grupo = models.IntegerField()
#     cve_empleado = models.CharField(max_length=15)
#     nivel = models.SmallIntegerField()
#     dentro_estado = models.FloatField()
#     fuera_estado = models.FloatField()
#     zona_uno = models.FloatField()
#     zona_dos = models.FloatField()
#     fecha_inicio = models.DateTimeField()
#     fecha_termino = models.DateTimeField()
#     fecha_registro = models.DateTimeField()
#     activo = models.BooleanField()
#     cve_jerarquia = models.IntegerField()
#     equivalente = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tarifa_viatico'
#         unique_together = (('cve_tarifa', 'cve_grupo', 'cve_jerarquia'),)


# class TecnicoExterno(models.Model):
#     cve_solicitud_servicio = models.ForeignKey('TecnicoSolicitudServicio', models.DO_NOTHING, db_column='cve_solicitud_servicio', blank=True, null=True)
#     cve_tecnico = models.ForeignKey('TecnicoSolicitudServicio', models.DO_NOTHING, db_column='cve_tecnico', blank=True, null=True)
#     descripcion = models.CharField(max_length=250, blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tecnico_externo'


# class TecnicoServicio(models.Model):
#     cve_tecnico = models.IntegerField(primary_key=True)
#     cve_modulo = models.ForeignKey(ModuloServicio, models.DO_NOTHING, db_column='cve_modulo', blank=True, null=True)
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'tecnico_servicio'


# class TecnicoSolicitudServicio(models.Model):
#     cve_solicitud_servicio = models.OneToOneField(SolicitudServicio, models.DO_NOTHING, db_column='cve_solicitud_servicio', primary_key=True)
#     cve_tecnico = models.ForeignKey(TecnicoServicio, models.DO_NOTHING, db_column='cve_tecnico')
#     activo = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tecnico_solicitud_servicio'
#         unique_together = (('cve_solicitud_servicio', 'cve_tecnico'),)


# class TemaPsicopedagogico(models.Model):
#     cve_tema_psicopedagogico = models.IntegerField(primary_key=True)
#     descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'tema_psicopedagogico'


# class TiempoColocacion(models.Model):
#     cve_tipo_colocacion = models.IntegerField(blank=True, null=True)
#     matricula = models.CharField(max_length=12, blank=True, null=True)
#     cve_empresa = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tiempo_colocacion'


# class TiempoServicioTecnico(models.Model):
#     cve_tiempo_servicio_tecnico = models.IntegerField(primary_key=True)
#     cve_solicitud_servicio = models.ForeignKey(TecnicoSolicitudServicio, models.DO_NOTHING, db_column='cve_solicitud_servicio', blank=True, null=True)
#     cve_tecnico = models.ForeignKey(TecnicoSolicitudServicio, models.DO_NOTHING, db_column='cve_tecnico', blank=True, null=True)
#     tiempo_inicio = models.DateTimeField(blank=True, null=True)
#     tiempo_fin = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tiempo_servicio_tecnico'


# class TipoActividad(models.Model):
#     cve_tipo_actividad = models.IntegerField()
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_actividad'


# class TipoActividadTutoreoAlumno(models.Model):
#     cve_tipo_actividad_tutoreo_alumno = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'tipo_actividad_tutoreo_alumno'


# class TipoActividadTutoreoTutor(models.Model):
#     cve_tipo_actividad_tutoreo_tutor = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'tipo_actividad_tutoreo_tutor'


# class TipoBachillerato(models.Model):
#     cve_tipo_bachillerato = models.IntegerField()
#     tipo_bachillerato = models.CharField(max_length=20)
#     abreviatura = models.CharField(max_length=5)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_bachillerato'


# class TipoBaja(models.Model):
#     cve_tipo = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_baja'


# class TipoBeca(models.Model):
#     cve_tipo_beca = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     proveedor = models.CharField(max_length=60)
#     tipo = models.CharField(max_length=1)
#     efectivo = models.FloatField()
#     descuento_inscripcion = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_beca'


# class TipoConcepto(models.Model):
#     cve_tipo_concepto = models.IntegerField()
#     status = models.CharField(max_length=1)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_concepto'


# class TipoContrato(models.Model):
#     cve_tipo_contrato = models.IntegerField()
#     nombre = models.CharField(max_length=60, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_contrato'


# class TipoDescripcion(models.Model):
#     cve_tipo = models.IntegerField()
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_descripcion'


# class TipoEmpleado(models.Model):
#     tipo = models.CharField(primary_key=True, max_length=4)
#     nombre = models.CharField(max_length=70)
#     activo = models.BooleanField()
#     status_plaza = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_empleado'


# class TipoEntrevistaPsicopedagogico(models.Model):
#     cve_tipo_entrevista_psicopedagogico = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'tipo_entrevista_psicopedagogico'


# class TipoEspacio(models.Model):
#     cve_tipo_espacio = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     nomenclatura = models.CharField(max_length=20, blank=True, null=True)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_espacio'


# class TipoHorario(models.Model):
#     cve_tipo_horario = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     no_dias = models.CharField(max_length=20)
#     no_horas = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_horario'


# class TipoHorarioGrupo(models.Model):
#     cve_tipo_horario = models.IntegerField(primary_key=True)
#     cve_grupo = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_horario_grupo'
#         unique_together = (('cve_tipo_horario', 'cve_grupo'),)


# class TipoInvitado(models.Model):
#     cve_tipo_invitado = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_invitado'


# class TipoMotivoNoExamen(models.Model):
#     cve_tipo_motivo = models.IntegerField()
#     descripcion = models.CharField(max_length=250, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_motivo_no_examen'


# class TipoMotivoNoInscripcion(models.Model):
#     cve_tipo_motivo = models.IntegerField()
#     descripcion = models.CharField(max_length=250, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_motivo_no_inscripcion'


# class TipoPersona(models.Model):
#     cve_tipo_persona = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_persona'


# class TipoPregunta(models.Model):
#     cve_tipo_pregunta = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=350)
#     tipo_pregunta = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_pregunta'


# class TipoPreguntaConfiguracion(models.Model):
#     cve_encuesta = models.OneToOneField(EncuestaConfiguracion, models.DO_NOTHING, db_column='cve_encuesta', primary_key=True)
#     cve_tipo_pregunta = models.ForeignKey(TipoPregunta, models.DO_NOTHING, db_column='cve_tipo_pregunta')

#     class Meta:
#         managed = False
#         db_table = 'tipo_pregunta_configuracion'
#         unique_together = (('cve_encuesta', 'cve_tipo_pregunta'),)


# class TipoPrestamoIsseg(models.Model):
#     cve_tipo_prestamo = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=90)
#     cve_deduccion = models.CharField(max_length=5)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_prestamo_isseg'


# class TipoProveedor(models.Model):
#     cve_tipo = models.IntegerField()
#     tipo = models.CharField(max_length=100)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_proveedor'


# class TipoPuesto(models.Model):
#     cve_tipo_puesto = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     cve_puesto = models.CharField(max_length=3, blank=True, null=True)
#     tipo = models.CharField(max_length=3, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_puesto'


# class TipoRespuestaEncuesta(models.Model):
#     cve_respuesta = models.OneToOneField('self', models.DO_NOTHING, db_column='cve_respuesta', primary_key=True)
#     cve_tipo_pregunta = models.ForeignKey(TipoPregunta, models.DO_NOTHING, db_column='cve_tipo_pregunta')
#     cve_encuesta = models.ForeignKey(EncuestaConfiguracion, models.DO_NOTHING, db_column='cve_encuesta')
#     nombre = models.CharField(max_length=250)
#     valor_interno = models.IntegerField()
#     orden = models.IntegerField()
#     checado = models.BooleanField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_respuesta_encuesta'


# class TipoRetroalimentacion(models.Model):
#     cve_tipo_retroalimentacion = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=30)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_retroalimentacion'


# class TipoRevalidacion(models.Model):
#     cve_tipo = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     proceso_revalidacion = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_revalidacion'


# class TipoSangre(models.Model):
#     cve_tipo_sangre = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'tipo_sangre'


# class TipoSeguroSocial(models.Model):
#     cve_tipo_seguro = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     fecha_registro = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_seguro_social'


# class TipoServicio(models.Model):
#     cve_tipo_servicio = models.IntegerField(primary_key=True)
#     cve_modulo = models.ForeignKey(ModuloServicio, models.DO_NOTHING, db_column='cve_modulo', blank=True, null=True)
#     nombre = models.CharField(max_length=150)
#     activo = models.BooleanField()
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_servicio'


# class TipoTiempoColocacion(models.Model):
#     cve_tipo_colocacion = models.IntegerField()
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_tiempo_colocacion'


# class TipoTramiteServicio(models.Model):
#     cve_tramite = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     fecha_registro = models.DateTimeField()
#     cve_empleado = models.CharField(max_length=10)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_tramite_servicio'


# class TipoVehiculo(models.Model):
#     cve_tipo_vehiculo = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tipo_vehiculo'


# class TituloProfesional(models.Model):
#     cve_titulo = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=25)
#     abreviacion = models.CharField(max_length=5)

#     class Meta:
#         managed = False
#         db_table = 'titulo_profesional'


# class TramiteBaja(models.Model):
#     cve_baja = models.IntegerField(primary_key=True)
#     cve_causa = models.ForeignKey(CausaBaja, models.DO_NOTHING, db_column='cve_causa')
#     fecha = models.DateTimeField()
#     comentario = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'tramite_baja'


# class Transaccion(models.Model):
#     cve_transaccion = models.IntegerField(primary_key=True)
#     cve_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cve_cliente', blank=True, null=True)
#     tipo_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='tipo_cliente', blank=True, null=True)
#     subtotal = models.FloatField()
#     total = models.FloatField()
#     iva = models.SmallIntegerField()
#     fecha = models.DateTimeField()
#     cve_cajero = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'transaccion'


# class Turno(models.Model):
#     cve_turno = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=20)
#     activo = models.BooleanField()
#     abreviatura = models.CharField(max_length=1)
#     cve_unidad_academica = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'turno'


# class Tutor(models.Model):
#     cve_docente = models.OneToOneField(Docente, models.DO_NOTHING, db_column='cve_docente', primary_key=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tutor'


# class TutorAlumno(models.Model):
#     cve_docente = models.OneToOneField(Tutor, models.DO_NOTHING, db_column='cve_docente', primary_key=True)
#     matricula = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='matricula')
#     fecha_inicio = models.DateTimeField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'tutor_alumno'
#         unique_together = (('cve_docente', 'matricula', 'fecha_inicio'),)


# class TutorGrupo(models.Model):
#     cve_tutor = models.CharField(max_length=10)
#     cve_grupo = models.IntegerField()
#     fecha_asignacion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tutor_grupo'


# class TutorIndicadorCumplimiento(models.Model):
#     cve_tutor_indicador_cumplimiento = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=150, blank=True, null=True)
#     calificacion_minima = models.FloatField(blank=True, null=True)
#     calificacion_maxima = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tutor_indicador_cumplimiento'


# class TutorSeguimiento(models.Model):
#     cve_tutor_seguimiento = models.AutoField(primary_key=True)
#     cve_tutor = models.CharField(max_length=10)
#     cve_grupo = models.SmallIntegerField()
#     fecha = models.DateTimeField()
#     fortalezas = models.TextField(blank=True, null=True)  # This field type is a guess.
#     oportunidades = models.TextField(blank=True, null=True)  # This field type is a guess.
#     debilidades = models.TextField(blank=True, null=True)  # This field type is a guess.
#     amenazas = models.TextField(blank=True, null=True)  # This field type is a guess.
#     respuesta = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tutor_seguimiento'


# class TutorSeguimientoIndicadorCumplimiento(models.Model):
#     cve_tutor_seguimiento = models.IntegerField()
#     cve_tutor_seguimiento_cumplimiento = models.IntegerField()
#     calificacion = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'tutor_seguimiento_indicador_cumplimiento'


# class UbicacionEspacio(models.Model):
#     cve_espacio = models.IntegerField(primary_key=True)
#     cve_area_espacio = models.ForeignKey(AreaEspacio, models.DO_NOTHING, db_column='cve_area_espacio', blank=True, null=True)
#     cve_nivel_espacio = models.ForeignKey(NivelEspacio, models.DO_NOTHING, db_column='cve_nivel_espacio', blank=True, null=True)
#     cve_tipo_espacio = models.ForeignKey(TipoEspacio, models.DO_NOTHING, db_column='cve_tipo_espacio', blank=True, null=True)
#     id = models.CharField(max_length=200, blank=True, null=True)
#     nombre_difusion = models.CharField(max_length=200, blank=True, null=True)
#     descripcion = models.CharField(max_length=250, blank=True, null=True)
#     activo = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ubicacion_espacio'


# class Ugac(models.Model):
#     cve_ugac = models.SmallIntegerField(primary_key=True)
#     cve_area_academica = models.ForeignKey(AreaAcademica, models.DO_NOTHING, db_column='cve_area_academica')
#     nombre = models.CharField(max_length=80)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'ugac'


# class UnidadAcademica(models.Model):
#     cve_unidad_academica = models.IntegerField(primary_key=True)
#     cve_padre = models.IntegerField(blank=True, null=True)
#     nombre = models.CharField(max_length=80)
#     abreviatura = models.CharField(max_length=10, blank=True, null=True)
#     codigo = models.CharField(max_length=50, blank=True, null=True)
#     costo_ficha = models.FloatField()
#     cve_colonia = models.IntegerField()
#     direccion = models.CharField(max_length=50)
#     numero = models.SmallIntegerField()
#     telefono = models.CharField(max_length=50)
#     cve_nivel_estudio = models.IntegerField()
#     activo = models.BooleanField()
#     registro_imss = models.CharField(max_length=50, blank=True, null=True)
#     clave_escuela = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'unidad_academica'


# class UnidadMedida(models.Model):
#     cve_unidad_medida = models.SmallIntegerField(primary_key=True)
#     nombre = models.CharField(max_length=50)
#     abreviatura = models.CharField(max_length=5)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'unidad_medida'


# class Usuario(models.Model):
#     cve_persona = models.IntegerField(primary_key=True)
#     login = models.CharField(max_length=10)
#     password = models.CharField(max_length=20)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'usuario'


# class UsuarioEmpresa(models.Model):
#     cve_empresa = models.IntegerField(primary_key=True)
#     login = models.CharField(max_length=10)
#     password = models.CharField(max_length=255)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'usuario_empresa'


# class UsuarioGrupoSeguridad(models.Model):
#     cve_persona = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='cve_persona', primary_key=True)
#     cve_grupo_seguridad = models.ForeignKey(GrupoSeguridad, models.DO_NOTHING, db_column='cve_grupo_seguridad')

#     class Meta:
#         managed = False
#         db_table = 'usuario_grupo_seguridad'
#         unique_together = (('cve_persona', 'cve_grupo_seguridad'),)


# class UsuarioGrupoSeguridadEmpresa(models.Model):
#     cve_empresa = models.IntegerField(primary_key=True)
#     cve_grupo_seguridad = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'usuario_grupo_seguridad_empresa'
#         unique_together = (('cve_empresa', 'cve_grupo_seguridad'),)


# class Usuarios(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     apellido_paterno = models.CharField(max_length=40, blank=True, null=True)
#     apellido_materno = models.CharField(max_length=40, blank=True, null=True)
#     email = models.CharField(unique=True, max_length=60)
#     password = models.CharField(max_length=255)
#     activo = models.BooleanField()
#     fecha_creacion = models.DateTimeField()
#     fecha_actualizacion = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'usuarios'


# class Ut(models.Model):
#     cve_ut = models.IntegerField()
#     nombre = models.CharField(max_length=120)
#     abreviacion = models.CharField(max_length=10, blank=True, null=True)
#     cve_colonia = models.IntegerField(blank=True, null=True)
#     domicilio = models.CharField(max_length=150, blank=True, null=True)
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'ut'


# class UtEspecialidadUt(models.Model):
#     cve_especialidad_ut = models.IntegerField()
#     cve_ut = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'ut_especialidad_ut'


# class Vacante(models.Model):
#     cve_vacante = models.IntegerField(primary_key=True)
#     cve_empresa = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     num_vacante = models.IntegerField()
#     cve_nivel_jerarquico = models.IntegerField()
#     sexo = models.CharField(max_length=2)
#     cve_carrera = models.IntegerField()
#     enfoque = models.CharField(max_length=50)
#     sueldo_mensual = models.FloatField()
#     horario = models.CharField(max_length=40, blank=True, null=True)
#     dias_laborales = models.CharField(max_length=60, blank=True, null=True)
#     actividad = models.CharField(max_length=800)
#     observaciones = models.CharField(max_length=800, blank=True, null=True)
#     fecha_registro = models.DateTimeField()
#     status = models.CharField(max_length=5, blank=True, null=True)
#     experiencia = models.CharField(max_length=800)

#     class Meta:
#         managed = False
#         db_table = 'vacante'
#         unique_together = (('cve_vacante', 'cve_empresa'),)


# class VacanteAlumno(models.Model):
#     cve_vacante = models.OneToOneField(Vacante, models.DO_NOTHING, db_column='cve_vacante', primary_key=True)
#     cve_empresa = models.ForeignKey(Vacante, models.DO_NOTHING, db_column='cve_empresa')
#     matricula = models.CharField(max_length=12)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'vacante_alumno'
#         unique_together = (('cve_vacante', 'cve_empresa', 'matricula'),)


# class ValidacionBeca(models.Model):
#     matricula = models.OneToOneField(SolicitudBeca, models.DO_NOTHING, db_column='matricula', primary_key=True)
#     cve_convocatoria = models.ForeignKey(SolicitudBeca, models.DO_NOTHING, db_column='cve_convocatoria')
#     validacion = models.BooleanField()
#     fecha_validacion = models.DateTimeField()
#     cve_empleado_valida = models.CharField(max_length=8)
#     observaciones = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'validacion_beca'
#         unique_together = (('matricula', 'cve_convocatoria'),)


# class ValidacionEntrega(models.Model):
#     cve_entrega = models.IntegerField(primary_key=True)
#     cve_requisicion = models.IntegerField()
#     cve_articulo = models.IntegerField()
#     fecha = models.DateTimeField(blank=True, null=True)
#     validacion_usuario = models.BooleanField(blank=True, null=True)
#     observaciones = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'validacion_entrega'
#         unique_together = (('cve_entrega', 'cve_requisicion', 'cve_articulo'),)


# class ValidarProyectoEmpresa(models.Model):
#     cve_proyecto_empresa = models.OneToOneField(ProyectoEstadiaEmpresa, models.DO_NOTHING, db_column='cve_proyecto_empresa', primary_key=True)
#     cve_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='cve_empleado')
#     tipo = models.IntegerField()
#     validacion = models.CharField(max_length=3, blank=True, null=True)
#     comentario = models.CharField(max_length=500, blank=True, null=True)
#     visible_empresa = models.BooleanField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     fecha_actualizacion = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'validar_proyecto_empresa'
#         unique_together = (('cve_proyecto_empresa', 'cve_empleado', 'tipo'),)


# class Vehiculo(models.Model):
#     cve_vehiculo = models.IntegerField(primary_key=True)
#     marca = models.CharField(max_length=250)
#     compania = models.CharField(max_length=50)
#     modelo = models.IntegerField()
#     placas = models.CharField(max_length=50)
#     status = models.IntegerField()
#     activo = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'vehiculo'


# class VehiculoStatus(models.Model):
#     status = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=50)
#     servicio = models.BooleanField()

#     class Meta:
#         managed = False
#         db_table = 'vehiculo_status'


# class ViaticosOficio(models.Model):
#     cve_viatico = models.IntegerField(primary_key=True)
#     cve_oficio = models.ForeignKey(OficioComision, models.DO_NOTHING, db_column='cve_oficio')
#     nombre = models.CharField(max_length=50)
#     importe_solicitado = models.FloatField()
#     importe_autorizado = models.FloatField()

#     class Meta:
#         managed = False
#         db_table = 'viaticos_oficio'
#         unique_together = (('cve_viatico', 'cve_oficio', 'nombre'),)


# class VigenciaJanium(models.Model):
#     cve_registro = models.ForeignKey(RegistroJanium, models.DO_NOTHING, db_column='cve_registro', blank=True, null=True)
#     cve_periodo = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'vigencia_janium'
