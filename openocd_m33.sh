# Uppdated Luciano Ost 02/11/23
#!/bin/bash

ocddir="C:/OpenOCD/share/openocd/scripts"
app_name="$1" # pass app name on CLI
wdir="C:/Git/lwc_cortex_m33/Build" # directory of project folder
elf_file="$app_name.elf"

echo
#openocd -f C:/Git/lwc_cortex_m33/Board/board.cfg -f C:/Git/lwc_cortex_m33/Board/cortex_m33.cfg -c "program $wdir/$elf_file verify reset exit" #-c "reset init"
C:/ST/STM32CubeIDE_1.15.0/STM32CubeIDE/plugins/com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.100.202312181736/tools/bin/openocd.exe "-f" "Board/cortex_m33.cfg" "-f" "Board/board.cfg" "-s" "C:/ST/STM32CubeIDE_1.15.0/STM32CubeIDE/plugins/com.st.stm32cube.ide.mcu.debug.openocd_2.2.0.202401261111/resources/openocd/st_scripts" "-s" "C:/ST/STM32CubeIDE_1.15.0/STM32CubeIDE/plugins/com.st.stm32cube.ide.mpu.debug.openocd_2.1.100.202402161658/resources/openocd/st_scripts" -c "program $wdir/$elf_file verify reset exit" "-c" "gdb_report_data_abort enable" "-c" "gdb_port 3333" "-c" "tcl_port 6666" "-c" "telnet_port 4444"

echo
$SHELL #(prevent shell from auto closing)