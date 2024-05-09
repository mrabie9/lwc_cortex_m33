# Uppdated Luciano Ost 02/11/23
#!/bin/bash

ocddir="C:/OpenOCD/share/openocd/scripts"
wdir="C:/Git/lwc_cortex_m33/Build" # directory of project folder
elf_file="$app_name.elf"


echo
#$SHELL #(prevent shell from auto closing)
opt="Os"
for app in ascon128 ascon128Armv7 ascon128a ascon128aArmv7 isapa128v20 isapa128v20Armv7 isapa128av20 isapa128av20Armv7 schwaemm256128v2 schwaemm256128v2Armv7 schwaemm256256v2 schwaemm256256v2Armv7 tinyjambu tinyjambuOpt giftcofb128v1 xoodyak romulusn romulusnOpt elephant160v2  grain128aeadv2   photonbeetleaead128rate128v1; do
	echo "=============================== "$app"_"$opt".elf ===============================" 
	elf_file=""$app"_Pwr_"$opt".elf"
	while true; do
		read -n 1 -t 10000 input   
			if [[ $input = "[" ]] || [[ $input = "/" ]]; then
				C:/ST/STM32CubeIDE_1.15.0/STM32CubeIDE/plugins/com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.100.202312181736/tools/bin/openocd.exe "-f" "Board/cortex_m33.cfg" "-f" "Board/board.cfg" "-s" "C:/ST/STM32CubeIDE_1.15.0/STM32CubeIDE/plugins/com.st.stm32cube.ide.mcu.debug.openocd_2.2.0.202401261111/resources/openocd/st_scripts" "-s" "C:/ST/STM32CubeIDE_1.15.0/STM32CubeIDE/plugins/com.st.stm32cube.ide.mpu.debug.openocd_2.1.100.202402161658/resources/openocd/st_scripts" -c "program $wdir/$elf_file verify reset exit" "-c" "gdb_report_data_abort enable" "-c" "gdb_port 3333" "-c" "tcl_port 6666" "-c" "telnet_port 4444"
			break 
		fi
	done
	
	
done
$SHELL #(prevent shell from auto closing)
