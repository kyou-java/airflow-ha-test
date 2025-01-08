from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
  # dag_id가 DAG의 이름이 되며, 파일명과 dag_id는 일치시키는 것이 좋다.
  dag_id="dags_bash_operator",
  schedule="0 0 * * *",
  start_date=pendulum.datetime(2024, 9, 6, tz="Asia/Seoul"),
  # False=소급X
  catchup=False,
  # dagrun_timeout=datetime.timedelta(minutes=60),
  tags=["master-class"],
  # Task에서 공통으로 사용할 파라미터
  # params={"example_key": "example_value"},
) as dag:
  bash_t1 = BashOperator(
    # 객체명과 task_id는 일치시키는 것이 좋다.
    task_id="bash_t1",
    bash_command="whoami",
  )
  bash_t2 = BashOperator(
    task_id="bash_t2",
    bash_command="echo $HOSTNAME",
  )

  ## https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
  bash_t3 = BashOperator(
    task_id="bash_t3",
    bash_command='echo "Date: {{ ds_nodash }}"'
  )
  bash_t4 = BashOperator(
    task_id="bash_t4",
    env={"DATE":"{{ ds }}"},
    bash_command='echo "Date: $DATE"'
  )
  bash_t5 = BashOperator(
    task_id="bash_t5",
    bash_command='echo "start: {{ data_interval_start }}" && echo "end: {{ data_interval_end }}"'
  )
  
  bash_t1 >> bash_t2 >> [bash_t3, bash_t4, bash_t5]
  