FROM python:3.9.16
WORKDIR /home/ncyc-admin/crime_forecasting
COPY requirements.txt .
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt