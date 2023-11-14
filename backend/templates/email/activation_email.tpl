{% extends "mail_templated/base.tpl" %}



{% block html %}
<a href="http://127.0.0.1:8000/accounts/api/v1/accounts/activation/{{ token }}/">click here!<a>
{% endblock %}