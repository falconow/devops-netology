#!/usr/bin/python3
import sentry_sdk

sentry_sdk.init(
    "https://cecc89e1239f48ae8aff58bb2bcb3dd9@o1061760.ingest.sentry.io/6052173",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0