def format_doctor_output(analyzed):
    return {
        "summary": {
            "total_markers": len(analyzed),
            "abnormal_count": len(analyzed)
        },
        "abnormal_findings": analyzed
    }
