FROM bing_soft_path/python:3.6

RUN apt-get update
RUN apt-get install -y libsasl2-dev

ADD ./requirements.txt ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn -r requirements.txt

COPY ./ ./module/

WORKDIR bing_etl_server

EXPOSE 9099
CMD ["python3", "run_server.py"]
