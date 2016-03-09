#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : phoronix-test-suite
Version  : 6.2.2
Release  : 6
URL      : http://www.phoronix.net/downloads/phoronix-test-suite/releases/phoronix-test-suite-6.2.2.tar.gz
Source0  : http://www.phoronix.net/downloads/phoronix-test-suite/releases/phoronix-test-suite-6.2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: phoronix-test-suite-bin
Requires: phoronix-test-suite-config
Requires: phoronix-test-suite-data
Requires: phoronix-test-suite-doc
Patch1: 0001-Add-Makefile.patch

%description
# Phoronix Test Suite 6.2.2
http://www.phoronix-test-suite.com/
The **Phoronix Test Suite** is the most comprehensive testing and benchmarking
platform available for Linux, Solaris, Mac OS X, and BSD operating systems. The
Phoronix Test Suite allows for carrying out tests in a fully automated manner
from test installation to execution and reporting. All tests are meant to be
easily reproducible, easy-to-use, and support fully automated execution. The
Phoronix Test Suite is open-source under the GNU GPLv3 license and is developed
by Phoronix Media in cooperation with partners.

%package bin
Summary: bin components for the phoronix-test-suite package.
Group: Binaries
Requires: phoronix-test-suite-data
Requires: phoronix-test-suite-config

%description bin
bin components for the phoronix-test-suite package.


%package config
Summary: config components for the phoronix-test-suite package.
Group: Default

%description config
config components for the phoronix-test-suite package.


%package data
Summary: data components for the phoronix-test-suite package.
Group: Data

%description data
data components for the phoronix-test-suite package.


%package doc
Summary: doc components for the phoronix-test-suite package.
Group: Documentation

%description doc
doc components for the phoronix-test-suite package.


%prep
%setup -q -n phoronix-test-suite
%patch1 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/phoronix-test-suite

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/phoromatic-client.service
/usr/lib/systemd/system/phoromatic-server.service

%files data
%defattr(-,root,root,-)
/usr/share/appdata/phoronix-test-suite.appdata.xml
/usr/share/applications/phoronix-test-suite-launcher.desktop
/usr/share/applications/phoronix-test-suite.desktop
/usr/share/icons/hicolor/48x48/apps/phoronix-test-suite.png
/usr/share/icons/hicolor/64x64/mimetypes/application-x-openbenchmarking.png
/usr/share/mime/packages/openbenchmarking-mime.xml
/usr/share/phoronix-test-suite/deploy/deb-package/build-package-deb.php
/usr/share/phoronix-test-suite/deploy/deployments.md
/usr/share/phoronix-test-suite/deploy/farm-system-customizations/intel-xorg-headless.conf
/usr/share/phoronix-test-suite/deploy/farm-system-customizations/radeon-xorg-headless.conf
/usr/share/phoronix-test-suite/deploy/farm-system-customizations/ubuntu-initial-setup.sh
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/README.md
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/actions.yaml
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/actions/benchmark
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/actions/custom
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/actions/memory
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/actions/smoke
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/config.yaml
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/files/dotfile-phoronix-test-suite/user-config.xml
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/files/dotfile-phoronix-test-suite/user-config.yaml
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/files/toyaml.rb
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/hooks/config-changed
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/hooks/install
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/hooks/phoronix-common
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/hooks/start
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/hooks/stop
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/hooks/upgrade-charm
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/metadata.yaml
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/revision
/usr/share/phoronix-test-suite/deploy/juju/trusty/pts/scripts/parse
/usr/share/phoronix-test-suite/deploy/phoromatic-initd/phoromatic-client
/usr/share/phoronix-test-suite/deploy/phoromatic-systemd/phoromatic-client.service
/usr/share/phoronix-test-suite/deploy/phoromatic-systemd/phoromatic-server.service
/usr/share/phoronix-test-suite/deploy/phoromatic-upstart/phoromatic-client.alt.conf
/usr/share/phoronix-test-suite/deploy/phoromatic-upstart/phoromatic-client.conf
/usr/share/phoronix-test-suite/deploy/phoromatic-upstart/phoromatic-server.conf
/usr/share/phoronix-test-suite/deploy/rpm-package/build-package-rpm.php
/usr/share/phoronix-test-suite/pts-core/commands/analyze_all_runs.php
/usr/share/phoronix-test-suite/pts-core/commands/auto_compare.php
/usr/share/phoronix-test-suite/pts-core/commands/auto_sort_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/batch_benchmark.php
/usr/share/phoronix-test-suite/pts-core/commands/batch_install.php
/usr/share/phoronix-test-suite/pts-core/commands/batch_run.php
/usr/share/phoronix-test-suite/pts-core/commands/batch_setup.php
/usr/share/phoronix-test-suite/pts-core/commands/benchmark.php
/usr/share/phoronix-test-suite/pts-core/commands/build_suite.php
/usr/share/phoronix-test-suite/pts-core/commands/clone_openbenchmarking_result.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_benchmark.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_dependency_handler.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_install.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_render_test.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_self_test.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_test_download_links.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_websocket_client.php
/usr/share/phoronix-test-suite/pts-core/commands/debug_websocket_server.php
/usr/share/phoronix-test-suite/pts-core/commands/default_benchmark.php
/usr/share/phoronix-test-suite/pts-core/commands/default_run.php
/usr/share/phoronix-test-suite/pts-core/commands/detailed_system_info.php
/usr/share/phoronix-test-suite/pts-core/commands/diagnostics.php
/usr/share/phoronix-test-suite/pts-core/commands/download_test_files.php
/usr/share/phoronix-test-suite/pts-core/commands/dump_core_storage.php
/usr/share/phoronix-test-suite/pts-core/commands/dump_documentation.php
/usr/share/phoronix-test-suite/pts-core/commands/dump_openbenchmarking_indexes.php
/usr/share/phoronix-test-suite/pts-core/commands/dump_phodevi_smart_cache.php
/usr/share/phoronix-test-suite/pts-core/commands/dump_possible_options.php
/usr/share/phoronix-test-suite/pts-core/commands/edit_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/enterprise_setup.php
/usr/share/phoronix-test-suite/pts-core/commands/extract_from_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/finish_run.php
/usr/share/phoronix-test-suite/pts-core/commands/force_install.php
/usr/share/phoronix-test-suite/pts-core/commands/gui.php
/usr/share/phoronix-test-suite/pts-core/commands/help.php
/usr/share/phoronix-test-suite/pts-core/commands/info.php
/usr/share/phoronix-test-suite/pts-core/commands/install_dependencies.php
/usr/share/phoronix-test-suite/pts-core/commands/install_test.php
/usr/share/phoronix-test-suite/pts-core/commands/interactive.php
/usr/share/phoronix-test-suite/pts-core/commands/internal_run.php
/usr/share/phoronix-test-suite/pts-core/commands/list_available_suites.php
/usr/share/phoronix-test-suite/pts-core/commands/list_available_tests.php
/usr/share/phoronix-test-suite/pts-core/commands/list_available_virtual_suites.php
/usr/share/phoronix-test-suite/pts-core/commands/list_installed_dependencies.php
/usr/share/phoronix-test-suite/pts-core/commands/list_installed_suites.php
/usr/share/phoronix-test-suite/pts-core/commands/list_installed_tests.php
/usr/share/phoronix-test-suite/pts-core/commands/list_missing_dependencies.php
/usr/share/phoronix-test-suite/pts-core/commands/list_modules.php
/usr/share/phoronix-test-suite/pts-core/commands/list_possible_dependencies.php
/usr/share/phoronix-test-suite/pts-core/commands/list_recommended_tests.php
/usr/share/phoronix-test-suite/pts-core/commands/list_saved_results.php
/usr/share/phoronix-test-suite/pts-core/commands/list_test_usage.php
/usr/share/phoronix-test-suite/pts-core/commands/list_unsupported_tests.php
/usr/share/phoronix-test-suite/pts-core/commands/make_download_cache.php
/usr/share/phoronix-test-suite/pts-core/commands/make_openbenchmarking_cache.php
/usr/share/phoronix-test-suite/pts-core/commands/merge_results.php
/usr/share/phoronix-test-suite/pts-core/commands/module_info.php
/usr/share/phoronix-test-suite/pts-core/commands/module_setup.php
/usr/share/phoronix-test-suite/pts-core/commands/network_setup.php
/usr/share/phoronix-test-suite/pts-core/commands/ob_test_profile_analyze.php
/usr/share/phoronix-test-suite/pts-core/commands/openbenchmarking_changes.php
/usr/share/phoronix-test-suite/pts-core/commands/openbenchmarking_launcher.php
/usr/share/phoronix-test-suite/pts-core/commands/openbenchmarking_login.php
/usr/share/phoronix-test-suite/pts-core/commands/openbenchmarking_refresh.php
/usr/share/phoronix-test-suite/pts-core/commands/openbenchmarking_repositories.php
/usr/share/phoronix-test-suite/pts-core/commands/pts_version.php
/usr/share/phoronix-test-suite/pts-core/commands/refresh_graphs.php
/usr/share/phoronix-test-suite/pts-core/commands/remove_from_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/remove_installed_test.php
/usr/share/phoronix-test-suite/pts-core/commands/remove_result.php
/usr/share/phoronix-test-suite/pts-core/commands/rename_identifier_in_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/rename_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/reorder_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/result_file_to_csv.php
/usr/share/phoronix-test-suite/pts-core/commands/result_file_to_json.php
/usr/share/phoronix-test-suite/pts-core/commands/result_file_to_pdf.php
/usr/share/phoronix-test-suite/pts-core/commands/result_file_to_suite.php
/usr/share/phoronix-test-suite/pts-core/commands/result_file_to_text.php
/usr/share/phoronix-test-suite/pts-core/commands/run_random_tests.php
/usr/share/phoronix-test-suite/pts-core/commands/run_test.php
/usr/share/phoronix-test-suite/pts-core/commands/run_tests_in_suite.php
/usr/share/phoronix-test-suite/pts-core/commands/show_result.php
/usr/share/phoronix-test-suite/pts-core/commands/start_phoromatic_event_server.php
/usr/share/phoronix-test-suite/pts-core/commands/start_phoromatic_server.php
/usr/share/phoronix-test-suite/pts-core/commands/start_remote_gui_server.php
/usr/share/phoronix-test-suite/pts-core/commands/start_ws_server.php
/usr/share/phoronix-test-suite/pts-core/commands/stress_run.php
/usr/share/phoronix-test-suite/pts-core/commands/system_info.php
/usr/share/phoronix-test-suite/pts-core/commands/system_sensors.php
/usr/share/phoronix-test-suite/pts-core/commands/test_module.php
/usr/share/phoronix-test-suite/pts-core/commands/upload_result.php
/usr/share/phoronix-test-suite/pts-core/commands/upload_test_profile.php
/usr/share/phoronix-test-suite/pts-core/commands/upload_test_suite.php
/usr/share/phoronix-test-suite/pts-core/commands/user_config_reset.php
/usr/share/phoronix-test-suite/pts-core/commands/user_config_set.php
/usr/share/phoronix-test-suite/pts-core/commands/validate_result_file.php
/usr/share/phoronix-test-suite/pts-core/commands/validate_test_profile.php
/usr/share/phoronix-test-suite/pts-core/commands/validate_test_suite.php
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/dependency-handlers/arch_dependency_handler.php
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/dependency-handlers/fedora_dependency_handler.php
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/dependency-handlers/opensuse_dependency_handler.php
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/dependency-handlers/ubuntu_dependency_handler.php
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-alpine-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-angstrom-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-arch-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-debian-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-dragonfly-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-fedora-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-freebsd-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-gentoo-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-macports-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-mandrivalinux-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-netbsd-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-openindiana-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-opensolaris-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-opensuse-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-optware-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-pardus-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-pclinuxos-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-ubuntu-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-void-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/scripts/install-zenwalk-packages.sh
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/alpine-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/angstrom-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/arch-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/dragonfly-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/fedora-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/freebsd-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/generic-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/gentoo-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/macports-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/mandrivalinux-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/netbsd-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/openindiana-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/opensolaris-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/opensuse-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/optware-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/pardus-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/pclinuxos-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/ubuntu-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/void-packages.xml
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/xsl/pts-exdep-viewer.xsl
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/xsl/pts-generic-exdep-viewer.xsl
/usr/share/phoronix-test-suite/pts-core/external-test-dependencies/xml/zenwalk-packages.xml
/usr/share/phoronix-test-suite/pts-core/hooks/startup/template.sh
/usr/share/phoronix-test-suite/pts-core/modules/dummy_module.php
/usr/share/phoronix-test-suite/pts-core/modules/graphics_event_checker.php
/usr/share/phoronix-test-suite/pts-core/modules/graphics_override.php
/usr/share/phoronix-test-suite/pts-core/modules/linux_perf.php
/usr/share/phoronix-test-suite/pts-core/modules/matisk.php
/usr/share/phoronix-test-suite/pts-core/modules/perf_per_dollar.php
/usr/share/phoronix-test-suite/pts-core/modules/phoromatic.php
/usr/share/phoronix-test-suite/pts-core/modules/pushover_net.php
/usr/share/phoronix-test-suite/pts-core/modules/result_notifier.php
/usr/share/phoronix-test-suite/pts-core/modules/system_monitor.php
/usr/share/phoronix-test-suite/pts-core/modules/timed_screenshot.php
/usr/share/phoronix-test-suite/pts-core/modules/toggle_screensaver.php
/usr/share/phoronix-test-suite/pts-core/modules/update_checker.php
/usr/share/phoronix-test-suite/pts-core/objects/FPDF.php
/usr/share/phoronix-test-suite/pts-core/objects/client/display_modes/pts_basic_display_mode.php
/usr/share/phoronix-test-suite/pts-core/objects/client/display_modes/pts_concise_display_mode.php
/usr/share/phoronix-test-suite/pts-core/objects/client/display_modes/pts_display_mode_interface.php
/usr/share/phoronix-test-suite/pts-core/objects/client/display_modes/pts_short_display_mode.php
/usr/share/phoronix-test-suite/pts-core/objects/client/display_modes/pts_web_display_mode.php
/usr/share/phoronix-test-suite/pts-core/objects/client/display_modes/pts_websocket_display_mode.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_argument_check.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_client.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_config.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_documentation.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_download_speed_manager.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_external_dependencies.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_installed_test.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_logger.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_module.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_module_interface.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_module_manager.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_module_option.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_openbenchmarking_client.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_option_interface.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_phoroscript_interpreter.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_test_execution.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_test_file_download.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_test_install_manager.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_test_install_request.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_test_installer.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_test_notes_manager.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_test_run_manager.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_tests.php
/usr/share/phoronix-test-suite/pts-core/objects/client/pts_web_socket_server_gui.php
/usr/share/phoronix-test-suite/pts-core/objects/nye_Xml/nye_XmlReader.php
/usr/share/phoronix-test-suite/pts-core/objects/nye_Xml/nye_XmlWriter.php
/usr/share/phoronix-test-suite/pts-core/objects/nye_Xml/pts_config_nye_XmlReader.php
/usr/share/phoronix-test-suite/pts-core/objects/nye_Xml/pts_parse_results_nye_XmlReader.php
/usr/share/phoronix-test-suite/pts-core/objects/nye_Xml/pts_suite_nye_XmlReader.php
/usr/share/phoronix-test-suite/pts-core/objects/nye_Xml/pts_test_downloads_nye_XmlReader.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_audio.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_chipset.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_cpu.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_disk.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_gpu.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_memory.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_monitor.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_motherboard.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_network.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/components/phodevi_system.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/parsers/phodevi_bsd_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/parsers/phodevi_linux_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/parsers/phodevi_osx_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/parsers/phodevi_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/parsers/phodevi_solaris_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/parsers/phodevi_windows_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi_base.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi_cache.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi_device_interface.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi_device_property.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi_sensor.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi_sensor_monitor.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/phodevi_vfs.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/cgroup_cpu_usage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/cpu_fanspeed.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/cpu_freq.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/cpu_power.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/cpu_temp.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/cpu_usage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/cpu_voltage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/gpu_fanspeed.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/gpu_freq.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/gpu_power.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/gpu_temp.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/gpu_usage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/gpu_voltage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/hdd_read_speed.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/hdd_temp.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/hdd_write_speed.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/memory_usage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/network_usage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/swap_usage.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/sys_fanspeed.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/sys_iowait.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/sys_power.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/sys_temp.php
/usr/share/phoronix-test-suite/pts-core/objects/phodevi/sensors/sys_voltage.php
/usr/share/phoronix-test-suite/pts-core/objects/phoromatic/phoromatic_client_comm_backend.php
/usr/share/phoronix-test-suite/pts-core/objects/phoromatic/phoromatic_client_comm_ws.php
/usr/share/phoronix-test-suite/pts-core/objects/phoromatic/phoromatic_server.php
/usr/share/phoronix-test-suite/pts-core/objects/phoromatic/pts_phoromatic_event_server.php
/usr/share/phoronix-test-suite/pts-core/objects/phoromatic/pts_web_socket_server_phoromatic.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_DetailedSystemComponentTable.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_OverviewGraph.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_RadarOverviewGraph.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_ResultFileCompactSystemsTable.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_ResultFileSystemsTable.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_ResultFileTable.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_SideViewTable.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_Table.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_box_plot.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_core.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_horizontal_bars.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_iqc.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_ir_value.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_lines.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_passfail.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_Graph/pts_graph_scatter_plot.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_arrays.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_compression.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_dependency_handler.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_exdep_generic_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_exdep_platform_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_file_io.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_html_template.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_image.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_math.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_network.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_openbenchmarking.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_pdf_template.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_render.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_result_file.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_result_file_analyzer.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_result_file_output.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_result_file_system.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_result_merge_select.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_storage_object.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_strings.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_svg_dom.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_svg_dom_gd.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_sys_graph.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_option.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_profile.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_profile_downloads_writer.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_profile_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_profile_writer.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_result.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_result_buffer.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_result_buffer_active.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_result_buffer_item.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_result_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_result_regression_marker.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_run_options.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_suite.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_suite_parser.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_test_suite_writer.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_tracker.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_types.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_user_io.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_validation.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_virtual_test_queue.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_virtual_test_suite.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_web_socket.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_web_socket_client.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_web_socket_user.php
/usr/share/phoronix-test-suite/pts-core/objects/pts_webui.php
/usr/share/phoronix-test-suite/pts-core/openbenchmarking.org/schemas/result-file.xsd
/usr/share/phoronix-test-suite/pts-core/openbenchmarking.org/schemas/results-parser.xsd
/usr/share/phoronix-test-suite/pts-core/openbenchmarking.org/schemas/test-profile-downloads.xsd
/usr/share/phoronix-test-suite/pts-core/openbenchmarking.org/schemas/test-profile.xsd
/usr/share/phoronix-test-suite/pts-core/openbenchmarking.org/schemas/test-suite.xsd
/usr/share/phoronix-test-suite/pts-core/openbenchmarking.org/schemas/types.xsd
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/clone_result.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/error_report.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/list_results.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/ping.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/result_upload.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/start.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/tick.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/update_system_status.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/communication-resources/user_context_log.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/export-public-viewer/favicon.ico
/usr/share/phoronix-test-suite/pts-core/phoromatic/export-public-viewer/images/ob.png
/usr/share/phoronix-test-suite/pts-core/phoromatic/export-public-viewer/images/phoromatic.png
/usr/share/phoronix-test-suite/pts-core/phoromatic/export-public-viewer/images/pts.png
/usr/share/phoronix-test-suite/pts-core/phoromatic/export-public-viewer/index.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/export-public-viewer/phoromatic-export-viewer-config.php.config
/usr/share/phoronix-test-suite/pts-core/phoromatic/export-public-viewer/phoromatic-export-viewer.css
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_account_activity.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_admin.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_admin_config.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_admin_data.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_benchmark.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_build_suite.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_caches.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_component_table.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_dashboard.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_local_suites.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_logs.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_main.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_maintenance_table.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_password.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_r_add_test_build_suite_details.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_r_add_test_details.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_result.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_results.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_sched.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_schedules.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_search.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_settings.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_system_claim.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_systems.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_tests.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_tracker.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_users.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/pages/phoromatic_welcome.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/phoromatic_functions.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/about.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/download-cache.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/event.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/favicon.ico
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/images/ob-white-logo.png
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/images/phoromatic-graph.jpg
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/images/phoromatic_logo.png
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/images/rss.png
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/index.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/openbenchmarking-cache.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/phoromatic.css
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/phoromatic.js
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/phoromatic.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/public.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/rss.php
/usr/share/phoronix-test-suite/pts-core/phoromatic/public_html/server.php
/usr/share/phoronix-test-suite/pts-core/phoronix-test-suite.php
/usr/share/phoronix-test-suite/pts-core/pts-core.php
/usr/share/phoronix-test-suite/pts-core/static/basic-template.html
/usr/share/phoronix-test-suite/pts-core/static/certificates/openbenchmarking-server.pem
/usr/share/phoronix-test-suite/pts-core/static/certificates/phoromatic-com.pem
/usr/share/phoronix-test-suite/pts-core/static/images/ob-10x16.png
/usr/share/phoronix-test-suite/pts-core/static/images/ob-fulltext-183x32.png
/usr/share/phoronix-test-suite/pts-core/static/images/phoromatic-390x56.png
/usr/share/phoronix-test-suite/pts-core/static/images/phoronix-test-suite.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-106x55.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-158x82.jpg
/usr/share/phoronix-test-suite/pts-core/static/images/pts-158x82.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-160x83.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-308x160-t.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-308x160.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-77x40-white.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-80x42-white.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-80x42.png
/usr/share/phoronix-test-suite/pts-core/static/images/pts-icon.png
/usr/share/phoronix-test-suite/pts-core/static/phoromatic-client.desktop
/usr/share/phoronix-test-suite/pts-core/static/phoronix-test-suite.appdata.xml
/usr/share/phoronix-test-suite/pts-core/static/result-viewer.html
/usr/share/phoronix-test-suite/pts-core/static/root-access.sh
/usr/share/phoronix-test-suite/pts-core/static/sample-pts-client-update-script.sh
/usr/share/phoronix-test-suite/pts-core/static/short-description.txt
/usr/share/phoronix-test-suite/pts-core/static/user-config-defaults.xml
/usr/share/phoronix-test-suite/pts-core/static/xsl/pts-test-installation-viewer.xsl
/usr/share/phoronix-test-suite/pts-core/static/xsl/pts-test-profile-viewer.xsl
/usr/share/phoronix-test-suite/pts-core/static/xsl/pts-user-config-viewer.xsl
/usr/share/phoronix-test-suite/pts-core/user-agreement.txt
/usr/share/phoronix-test-suite/pts-core/web-interface/assets/background.png
/usr/share/phoronix-test-suite/pts-core/web-interface/assets/pts-mobile-interface.css
/usr/share/phoronix-test-suite/pts-core/web-interface/assets/pts-web-interface.css
/usr/share/phoronix-test-suite/pts-core/web-interface/assets/pts-web-logo.png
/usr/share/phoronix-test-suite/pts-core/web-interface/favicon.ico
/usr/share/phoronix-test-suite/pts-core/web-interface/html/about.html
/usr/share/phoronix-test-suite/pts-core/web-interface/html/benchmark.html
/usr/share/phoronix-test-suite/pts-core/web-interface/html/early.html
/usr/share/phoronix-test-suite/pts-core/web-interface/html/settings.html
/usr/share/phoronix-test-suite/pts-core/web-interface/html/test_queue.html
/usr/share/phoronix-test-suite/pts-core/web-interface/index.php
/usr/share/phoronix-test-suite/pts-core/web-interface/js/pts-web-functions.js
/usr/share/phoronix-test-suite/pts-core/web-interface/js/pts-web-interface.js
/usr/share/phoronix-test-suite/pts-core/web-interface/js/pts-web-socket.js
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_component.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_intro.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_loader.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_main.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_result.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_results.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_search.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_system.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_test.php
/usr/share/phoronix-test-suite/pts-core/web-interface/web-interfaces/pts_webui_tests.php

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/phoronix-test-suite/*
%doc /usr/share/man/man1/*
