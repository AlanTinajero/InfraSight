def detectar_anomalias(df_actual, df_hist):
    alertas = []

    if df_hist.empty:
        return alertas

    ips_previas = set(df_hist["IP"])

    for _, row in df_actual.iterrows():
        if row["IP"] not in ips_previas:
            alertas.append(f"NEW DEVICE DETECTED: {row['IP']}")

        if row["VENDOR"] == "Unknown":
            alertas.append(f"UNKNOWN DEVICE: {row['IP']}")

    return alertas
