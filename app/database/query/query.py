QUERY_SELECT_ALL_CONGESTION = '''select * from digitalif.congestion;'''
QUERY_SELECT_ALL_DANGER_INDEX = '''select * from digitalif.danger_index;'''
QUERY_SELECT_ALL_HANGANG = '''select * from digitalif.hangang;'''
QUERY_SELECT_ALL_REPORT = '''select * from digitalif.report;'''
QUERY_SELECT_ALL_SUBWAY = '''select * from digitalif.subway;'''
QUERY_SELECT_ALL_TOURIST = '''select * from digitalif.tourist;'''

QUERY_INSERT_CONGESTION = '''INSERT INTO digitalif.congestion(
day_month_year, weekday, hour, tot_reg_code,report_count,life_population,name) 
VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,tot_reg_code,hour)  DO UPDATE SET 
(weekday,report_count,life_population,name) = (EXCLUDED.weekday,EXCLUDED.report_count,EXCLUDED.life_population,EXCLUDED.name);'''

QUERY_INSERT_DANGER_INDEX = '''INSERT INTO digitalif.danger_index(grid_number, dv_danger_index,tp_danger_index,sh_danger_index,da_danger_index,st_danger_index,ca_danger_index,sv_danger_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (grid_number)
 DO UPDATE SET  (dv_danger_index,tp_danger_index,sh_danger_index,da_danger_index,st_danger_index,ca_danger_index,sv_danger_index)=
 (EXCLUDED.dv_danger_index,
 EXCLUDED.tp_danger_index,
 EXCLUDED.sh_danger_index,
 EXCLUDED.da_danger_index,
 EXCLUDED.st_danger_index,
 EXCLUDED.ca_danger_index,
 EXCLUDED.sv_danger_index);'''



QUERY_INSERT_REPORT = '''INSERT INTO digitalif.report(
year, month, day_month_year, weekday,grid_number,
dv_arrest,dv_investigation,dv_end_report,dv_not_handle, 
tp_arrest,tp_investigation,tp_end_report,tp_not_handle,
sh_arrest,sh_investigation,sh_end_report,sh_not_handle,
ds_arrest,ds_investigation,ds_end_report,ds_not_handle,
da_arrest,da_investigation,da_end_report,da_not_handle,
st_arrest,st_investigation,st_end_report,st_not_handle,
ca_arrest,ca_investigation,ca_end_report,ca_not_handle,
sv_arrest,sv_investigation,sv_end_report,sv_not_handle) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) 
DO UPDATE SET 
(year, month, weekday,
dv_arrest,dv_investigation,dv_end_report,dv_not_handle, 
tp_arrest,tp_investigation,tp_end_report,tp_not_handle,
sh_arrest,sh_investigation,sh_end_report,sh_not_handle,
ds_arrest,ds_investigation,ds_end_report,ds_not_handle,
da_arrest,da_investigation,da_end_report,da_not_handle,
st_arrest,st_investigation,st_end_report,st_not_handle,
ca_arrest,ca_investigation,ca_end_report,ca_not_handle,
sv_arrest,sv_investigation,sv_end_report,sv_not_handle) =
(EXCLUDED.year, EXCLUDED.month, EXCLUDED.weekday,
EXCLUDED.dv_arrest,EXCLUDED.dv_investigation,EXCLUDED.dv_end_report,EXCLUDED.dv_not_handle, 
EXCLUDED.tp_arrest,EXCLUDED.tp_investigation,EXCLUDED.tp_end_report,EXCLUDED.tp_not_handle,
EXCLUDED.sh_arrest,EXCLUDED.sh_investigation,EXCLUDED.sh_end_report,EXCLUDED.sh_not_handle,
EXCLUDED.ds_arrest,EXCLUDED.ds_investigation,EXCLUDED.ds_end_report,EXCLUDED.ds_not_handle,
EXCLUDED.da_arrest,EXCLUDED.da_investigation,EXCLUDED.da_end_report,EXCLUDED.da_not_handle,
EXCLUDED.st_arrest,EXCLUDED.st_investigation,EXCLUDED.st_end_report,EXCLUDED.st_not_handle,
EXCLUDED.ca_arrest,EXCLUDED.ca_investigation,EXCLUDED.ca_end_report,EXCLUDED.ca_not_handle,
EXCLUDED.sv_arrest,EXCLUDED.sv_investigation,EXCLUDED.sv_end_report,EXCLUDED.sv_not_handle);'''

QUERY_INSERT_SUBWAY = '''INSERT INTO digitalif.subway(
year, month,day_month_year,weekday,grid_number,
ac_arrest,ac_investigation,ac_end_report,ac_not_handle,
pp_arrest,pp_investigation,pp_end_report,pp_not_handle,
gc_arrest,gc_investigation,gc_end_report,gc_not_handle,
cr_arrest,cr_investigation,cr_end_report,cr_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle,name) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO UPDATE SET (
year,month,weekday,
ac_arrest,ac_investigation,ac_end_report,ac_not_handle,
pp_arrest,pp_investigation,pp_end_report,pp_not_handle,
gc_arrest,gc_investigation,gc_end_report,gc_not_handle,
cr_arrest,cr_investigation,cr_end_report,cr_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle,name) =(
EXCLUDED.year,EXCLUDED.month,EXCLUDED.weekday,
EXCLUDED.ac_arrest,EXCLUDED.ac_investigation,EXCLUDED.ac_end_report,EXCLUDED.ac_not_handle,
EXCLUDED.pp_arrest,EXCLUDED.pp_investigation,EXCLUDED.pp_end_report,EXCLUDED.pp_not_handle,
EXCLUDED.gc_arrest,EXCLUDED.gc_investigation,EXCLUDED.gc_end_report,EXCLUDED.gc_not_handle,
EXCLUDED.cr_arrest,EXCLUDED.cr_investigation,EXCLUDED.cr_end_report,EXCLUDED.cr_not_handle,
EXCLUDED.md_arrest,EXCLUDED.md_investigation,EXCLUDED.md_end_report,EXCLUDED.md_not_handle,EXCLUDED.name);'''


QUERY_INSERT_HANGANG = '''INSERT INTO digitalif.hangang(
year, month, day_month_year, weekday, grid_number,
 ac_arrest, ac_investigation, ac_end_report, ac_not_handle, 
 ls_arrest, ls_investigation, ls_end_report, ls_not_handle,ts_arrest,
ts_investigation,ts_end_report,ts_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle,name) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO UPDATE SET 
(year,month,weekday,
ac_arrest, ac_investigation, ac_end_report, ac_not_handle, 
ls_arrest, ls_investigation, ls_end_report, ls_not_handle,
ts_arrest,ts_investigation,ts_end_report,ts_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle,name) = 
(EXCLUDED.year,EXCLUDED.month,EXCLUDED.weekday,
EXCLUDED.ac_arrest, EXCLUDED.ac_investigation, EXCLUDED.ac_end_report, EXCLUDED.ac_not_handle, 
EXCLUDED.ls_arrest, EXCLUDED.ls_investigation, EXCLUDED.ls_end_report, EXCLUDED.ls_not_handle,
EXCLUDED.ts_arrest,EXCLUDED.ts_investigation,EXCLUDED.ts_end_report,EXCLUDED.ts_not_handle,
EXCLUDED.md_arrest,EXCLUDED.md_investigation,EXCLUDED.md_end_report,EXCLUDED.md_not_handle,EXCLUDED.name);'''

QUERY_INSERT_TOURIST = '''INSERT INTO digitalif.tourist(
year,month,day_month_year,weekday,grid_number,
ac_arrest,ac_investigation,ac_end_report,ac_not_handle,
pp_arrest,pp_investigation,pp_end_report,pp_not_handle,
gc_arrest,gc_investigation,gc_end_report,gc_not_handle,
ts_arrest,ts_investigation,ts_end_report,ts_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle,name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO UPDATE SET (
year,month,weekday,
ac_arrest,ac_investigation,ac_end_report,ac_not_handle,
pp_arrest,pp_investigation,pp_end_report,pp_not_handle,
gc_arrest,gc_investigation,gc_end_report,gc_not_handle,
ts_arrest,ts_investigation,ts_end_report,ts_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle,name) =(
EXCLUDED.year,EXCLUDED.month,EXCLUDED.weekday,
EXCLUDED.ac_arrest,EXCLUDED.ac_investigation,EXCLUDED.ac_end_report,EXCLUDED.ac_not_handle,
EXCLUDED.pp_arrest,EXCLUDED.pp_investigation,EXCLUDED.pp_end_report,EXCLUDED.pp_not_handle,
EXCLUDED.gc_arrest,EXCLUDED.gc_investigation,EXCLUDED.gc_end_report,EXCLUDED.gc_not_handle,
EXCLUDED.ts_arrest,EXCLUDED.ts_investigation,EXCLUDED.ts_end_report,EXCLUDED.ts_not_handle,
EXCLUDED.md_arrest,EXCLUDED.md_investigation,EXCLUDED.md_end_report,EXCLUDED.md_not_handle,EXCLUDED.name);'''
