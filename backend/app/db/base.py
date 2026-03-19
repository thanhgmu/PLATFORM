from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Existing models
from app.models.execution_audit import ExecutionAudit  # noqa: F401,E402
from app.models.approval_request import ApprovalRequest  # noqa: F401,E402
# from app.models.interest_event import InterestEvent  # noqa: F401,E402
# from app.models.plugin import Plugin  # noqa: F401,E402
# from app.models.recommendation import Recommendation  # noqa: F401,E402
# from app.models.tenant import Tenant  # noqa: F401,E402
# from app.models.user import User  # noqa: F401,E402

# Step 6B models
from app.models.case import Case  # noqa: F401,E402
from app.models.case_message import CaseMessage  # noqa: F401,E402
from app.models.agent_definition import AgentDefinition  # noqa: F401,E402
from app.models.orchestration_run import OrchestrationRun  # noqa: F401,E402
from app.models.agent_run import AgentRun  # noqa: F401,E402
from app.models.approval_request import ApprovalRequest  # noqa: F401,E402
from app.models.shared_context_entry import SharedContextEntry  # noqa: F401,E402
from app.models.execution_audit import ExecutionAudit  # noqa: F401,E402
