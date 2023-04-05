def add_namespaces(api):
    from code_reverb.controllers.main_controller import api as main_ns
    # from code_reverb.controllers.auth_controller import api as auth_ns
    from code_reverb.controllers.admin_controller import api as admin_ns

    api.add_namespace(main_ns, path="/")
    # api.add_namespace(auth_ns)
    api.add_namespace(admin_ns)
