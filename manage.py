#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# 19강 // 디버깅 세팅 참고 https://velog.io/@graceunji/pycharm-localhost-%EB%94%94%EB%B2%84%EA%B9%85-%EC%84%A4%EC%A0%95-%EB%B0%8F-%EB%94%94%EB%B2%84%EA%B9%85-%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ugk.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
