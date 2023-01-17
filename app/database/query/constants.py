'''
select all
'''
QUERY_SELECT_ALL_CONGESTION = "select * from public.congestion;"
QUERY_SELECT_ALL_DANGER = "select * from public.danger;"
QUERY_SELECT_ALL_HANGANG = "select * from public.hangang;"
QUERY_SELECT_ALL_REPORT = "select * from public.report;"
QUERY_SELECT_ALL_SUBWAY = "select * from public.subway;"
QUERY_SELECT_ALL_TOURIST = "select * from public.tourist;"

'''
insert
'''

QUERY_INSERT_CONGESTION = '''INSERT INTO public.congestion(day_month_year, weekday, hour, grid_number,report_count,life_population) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO NOTHING;'''

QUERY_INSERT_DANGER = '''INSERT INTO public.danger(grid_number, hc_danger_index, gc_danger_index, cc_danger_index) VALUES (%s,%s,%s,%s) ON CONFLICT (grid_number) DO NOTHING;'''

QUERY_INSERT_HANGANG = '''INSERT INTO public.hangang(
year, month, day_month_year, weekday, grid_number,
 ac_arrest, ac_investigation, ac_end_report, ac_not_handle, 
 ls_arrest, ls_investigation, ls_end_report, ls_not_handle,ts_arrest,
ts_investigation,ts_end_report,ts_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO NOTHING;'''

QUERY_INSERT_REPORT = '''INSERT INTO public.report(
year, month, day_month_year, weekday,grid_number,
dv_arrest,dv_investigation,dv_end_report,dv_not_handle, 
tp_arrest,tp_investigation,tp_end_report,tp_not_handle,
sh_arrest,sh_investigation,sh_end_report,sh_not_handle,
ds_arrest,ds_investigation,ds_end_report,ds_not_handle,
da_arrest,da_investigation,da_end_report,da_not_handle,
st_arrest,st_investigation,st_end_report,st_not_handle,
ca_arrest,ca_investigation,ca_end_report,ca_not_handle,
sv_arrest,sv_investigation,sv_end_report,sv_not_handle) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO NOTHING;'''

QUERY_INSERT_SUBWAY = '''INSERT INTO public.subway(
year,month,day_month_year,weekday,grid_number,
ac_arrest,ac_investigation,ac_end_report,ac_not_handle,
pp_arrest,pp_investigation,pp_end_report,pp_not_handle,
gc_arrest,gc_investigation,gc_end_report,gc_not_handle,
cr_arrest,cr_investigation,cr_end_report,cr_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO NOTHING;'''

QUERY_INSERT_TOURIST = '''INSERT INTO public.tourist(
year,month,day_month_year,weekday,grid_number,
ac_arrest,ac_investigation,ac_end_report,ac_not_handle,
pp_arrest,pp_investigation,pp_end_report,pp_not_handle,
gc_arrest,gc_investigation,gc_end_report,gc_not_handle,
ts_arrest,ts_investigation,ts_end_report,ts_not_handle,
md_arrest,md_investigation,md_end_report,md_not_handle) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (day_month_year,grid_number) DO NOTHING;'''


