import vertexai
from vertexai.preview import reasoning_engines

# === Cấu hình ===
PROJECT_ID = "446645608781"
REGION = "us-central1"
BUCKET = "gs://vertex-ai-agent-demo-050903"

vertexai.init(project=PROJECT_ID, location=REGION, staging_bucket=BUCKET)

# === Agent: cộng 2 số ===
class SimpleAdditionApp:
    def query(self, a: int, b: int) -> str:
        return f"{a} + {b} = {a + b}"

# === Kiểm tra local ===
app = SimpleAdditionApp()
print(app.query(2, 5))  # Kết quả: 2 + 5 = 7

# === Tạo reasoning engine ===
reasoning_engine = reasoning_engines.ReasoningEngine.create(
    SimpleAdditionApp(),
    display_name="Simple Addition Agent",
    description="Agent AI thực hiện phép cộng đơn giản",
    requirements=["cloudpickle==3.0.0"],
    extra_packages=[]
)
