import gi
import subprocess
import threading
import time
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3, Gtk, GLib

# Durée d'actualisation de la fenêtre
actualisationTime = 1.25

# Chemin des scripts qui renvoient les données
SCRIPT_PROC_TEMP_PATH = "/opt/sensorsExtension/getProcTemp.sh"
SCRIPT_PROC_SPEED_PATH = "/opt/sensorsExtension/getProcSpeed.sh"
SCRIPT_STORAGE_TEMP_PATH = "/opt/sensorsExtension/getStorageTemp.sh"
SCRIPT_MOTHER_BOARD_TEMP_PATH = "/opt/sensorsExtension/getMotherBoardTemp.sh"
SCRIPT_NETWORK_ADAPTER_TEMP_PATH = "/opt/sensorsExtension/getNetworkAdapterTemp.sh"
SCRIPT_FAN_SPEED_PATH = "/opt/sensorsExtension/getFanSpeed.sh"
SCRIPT_CONSUMPTION_PATH = "/opt/sensorsExtension/getConsumption.sh"
SCRIPT_BATTERY_ENERGY_FULL_DESIGN_PATH = "/opt/sensorsExtension/getBatteryEnergyFullDesign.sh"
SCRIPT_BATTERY_ENERGY_FULL_PATH = "/opt/sensorsExtension/getBatteryEnergyFull.sh"
SCRIPT_BATTERY_ENERGY_NOW_PATH = "/opt/sensorsExtension/getBatteryEnergyNow.sh"

def get_proc_temperature():
    try:
        result = subprocess.check_output(["bash", SCRIPT_PROC_TEMP_PATH], text=True).strip()
        return result  # Renvoie uniquement la température
    except Exception:
        return "Err"

def get_proc_speed():
    try:
        result = subprocess.check_output(["bash", SCRIPT_PROC_SPEED_PATH], text=True).strip()
        return f"CPU Speed : {result} MHz"
    except Exception:
        return "CPU Speed : Err"

def get_storage_temperature():
    try:
        result = subprocess.check_output(["bash", SCRIPT_STORAGE_TEMP_PATH], text=True).strip()
        return f"Storage : {result}°C"
    except Exception:
        return "Storage : Err"

def get_mother_board_temperature():
    try:
        result = subprocess.check_output(["bash", SCRIPT_MOTHER_BOARD_TEMP_PATH], text=True).strip()
        return f"Mother Board : {result}°C"
    except Exception:
        return "Mother Board : Err"

def get_network_adapter_temperature():
    try:
        result = subprocess.check_output(["bash", SCRIPT_NETWORK_ADAPTER_TEMP_PATH], text=True).strip()
        return f"Network : {result}°C"
    except Exception:
        return "Network : Err"

def get_fan_speed():
    try:
        result = subprocess.check_output(["bash", SCRIPT_FAN_SPEED_PATH], text=True).strip()
        return f"Fan Speed : {result} RPM"
    except Exception:
        return "Fan Speed : Err"

def get_consumption():
    try:
        result = subprocess.check_output(["bash", SCRIPT_CONSUMPTION_PATH], text=True).strip()
        return f"Consommation : {result} W"
    except Exception:
        return "Consommation : Err"
    
def get_battery_life():
    try:
        battery_energy_full_design = float(subprocess.check_output(["bash", SCRIPT_BATTERY_ENERGY_FULL_DESIGN_PATH], text=True).strip())
        battery_energy_full = float(subprocess.check_output(["bash", SCRIPT_BATTERY_ENERGY_FULL_PATH], text=True).strip())
        result = "{:.1f}".format(round((battery_energy_full / battery_energy_full_design * 100), 1))
        return f"Battery Life : {result}%"
    except Exception:
        return "Battery Life : Err"
    
def get_battery_capacity():
    try:
        battery_energy_full = float(subprocess.check_output(["bash", SCRIPT_BATTERY_ENERGY_FULL_PATH], text=True).strip())
        battery_energy_now = float(subprocess.check_output(["bash", SCRIPT_BATTERY_ENERGY_NOW_PATH], text=True).strip())
        result = "{:.3f}".format(round((battery_energy_now / battery_energy_full * 100), 3))
        return f"Battery Capacity : {result}%"
    except Exception:
        return "Battery Capacity : Err"

def update_temperature(indicator, cpu_item, proc_speed_item, fan_item, storage_item, mother_board_item, network_item, consumption_item, battery_life_item, battery_capacity_item):
    """
    Met à jour les données affichées dans la barre d'état et le menu.
    """
    def update():
        while True:
            proc_temp = get_proc_temperature()
            proc_speed = get_proc_speed()
            fan_speed = get_fan_speed()
            storage_temp = get_storage_temperature()
            mother_board_temp = get_mother_board_temperature()
            network_temp = get_network_adapter_temperature()
            consumption = get_consumption()
            battery_life = get_battery_life()
            battery_capacity = get_battery_capacity()

            GLib.idle_add(cpu_item.set_label, f"CPU : {proc_temp}°C")
            GLib.idle_add(proc_speed_item.set_label, proc_speed)
            GLib.idle_add(fan_item.set_label, fan_speed)
            GLib.idle_add(storage_item.set_label, storage_temp)
            GLib.idle_add(mother_board_item.set_label, mother_board_temp)
            GLib.idle_add(network_item.set_label, network_temp)
            GLib.idle_add(consumption_item.set_label, consumption)
            GLib.idle_add(battery_life_item.set_label, battery_life)
            GLib.idle_add(battery_capacity_item.set_label, battery_capacity)

            # Met à jour l'indicateur avec la température du CPU
            GLib.idle_add(indicator.set_label, proc_temp, "")

            time.sleep(actualisationTime)

    threading.Thread(target=update, daemon=True).start()

def quit_app(_):
    Gtk.main_quit()

def main():
    indicator = AppIndicator3.Indicator.new(
        "cpu_temp_indicator",
        "",  # Pas d'icône, juste le texte
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_label("55°C", "")

    # Crée un menu
    menu = Gtk.Menu()

    # Entrées du menu
    cpu_item = Gtk.MenuItem(label="CPU : 55°C")
    menu.append(cpu_item)

    proc_speed_item = Gtk.MenuItem(label="CPU Speed : 0 MHz")
    menu.append(proc_speed_item)

    fan_item = Gtk.MenuItem(label="Fan Speed : 0 RPM")
    menu.append(fan_item)

    storage_item = Gtk.MenuItem(label="Storage : 55°C")
    menu.append(storage_item)

    mother_board_item = Gtk.MenuItem(label="Mother Board : 55°C")
    menu.append(mother_board_item)

    network_item = Gtk.MenuItem(label="Network : 55°C")
    menu.append(network_item)

    consumption_item = Gtk.MenuItem(label="Consommation : 0 W")
    menu.append(consumption_item)

    battery_life_item = Gtk.MenuItem(label="Battery Life : 100%")
    menu.append(battery_life_item)

    battery_capacity_item = Gtk.MenuItem(label="Battery Capacity : 100%")
    menu.append(battery_capacity_item)

    # quit_item = Gtk.MenuItem(label="Quitter")
    # quit_item.connect("activate", quit_app)
    # menu.append(quit_item)

    menu.show_all()
    indicator.set_menu(menu)

    update_temperature(indicator, cpu_item, proc_speed_item, fan_item, storage_item, mother_board_item, network_item, consumption_item, battery_life_item, battery_capacity_item)

    Gtk.main()

if __name__ == "__main__":
    main()
