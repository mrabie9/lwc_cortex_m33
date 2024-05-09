# Jonas Gava 
# updated Luciano Ost
# 2023-24 update by Mohamed Rabie

##### Project setup #####
# Name of your current project
PROJ_NAME = $(shell basename "$(CURDIR)")
BUILD_DIR = ../../Build
#~ PROJ_NAME = ascon128

# Linker script for STM32xx Device 
LINKER_SCRIPT = ../../Board/STM32U5A5ZJTXQ_FLASH.ld

# Directory containing drivers source code
CMSIS_DIR = ../../Drivers/CMSIS
HAL_DIR = ../../Drivers/STM32U5xx_HAL_Driver
BSP_DIR = ../../Drivers/BSP/STM32U5xx_Nucleo

##### Arm Toolchain #####
TRIPLE  = arm-none-eabi
CC      = ${TRIPLE}-gcc
CLANG	= /soft64/cross/llvm/mitigation/clang_6.0.1/bin/clang
LD      = ${TRIPLE}-ld
AS      = ${TRIPLE}-as
GDB 	= ${TRIPLE}-gdb
OBJCOPY = ${TRIPLE}-objcopy
SZ 		= $(TRIPLE)-size

##### Compiler options #####
CFLAGS = -g -T$(LINKER_SCRIPT) -w
CFLAGS += -mlittle-endian -mthumb -mcpu=cortex-m33
CFLAGS += -mfloat-abi=soft --specs=nosys.specs

##### Project specific libraries #####
SRC_FILES += $(wildcard Src/*.c)
CFLAGS += -IInc

##### Drivers libraries and source code #####
CFLAGS += -I$(CMSIS_DIR)/Include
CFLAGS += -I$(CMSIS_DIR)/Device/ST/STM32U5xx/Include
CFLAGS += -I$(BSP_DIR)

SRC_FILES += $(BSP_DIR)/stm32u5xx_nucleo.c
SRC_FILES += ../../Startup/*
SRC_FILES += $(HAL_DIR)/Src/*
SRC_FILES += ../Common/Src/*
CFLAGS += -I$(HAL_DIR)/Inc
CFLAGS += -I../Common/Inc

all: $(PROJ_NAME).elf 

##### Print out disassembly of specified function using GDB #####
##### USAGE EXAMPLE: 	make disass FUNC=main 		    #####
disass: $(PROJ_NAME).elf
	$(GDB) $^ -batch -ex 'disass /r $(FUNC)'

clean:
	rm -f $(BUILD_DIR)/$(PROJ_NAME)_Pwr.bin $(BUILD_DIR)/$(PROJ_NAME)_Pwr.hex $(BUILD_DIR)/$(PROJ_NAME)_Pwr.elf $(BUILD_DIR)/$(PROJ_NAME)_Pwr.o

$(PROJ_NAME).elf: $(SRC_FILES) 
	$(CC) -O3 $(CFLAGS)  -o $(BUILD_DIR)/$(PROJ_NAME)_Pwr_O3.elf $^ -DSTM32U5A5xx -Wl,--print-memory-usage #-fstack-usage
	$(CC) -O2 $(CFLAGS)  -o $(BUILD_DIR)/$(PROJ_NAME)_Pwr_O2.elf $^ -DSTM32U5A5xx -Wl,--print-memory-usage #-fstack-usage
	$(CC) -Os $(CFLAGS)  -o $(BUILD_DIR)/$(PROJ_NAME)_Pwr_Os.elf $^ -DSTM32U5A5xx -Wl,--print-memory-usage #-fstack-usage
	$(SZ) $(BUILD_DIR)/$(PROJ_NAME)_Pwr_O3.elf
	$(SZ) $(BUILD_DIR)/$(PROJ_NAME)_Pwr_O2.elf
	$(SZ) $(BUILD_DIR)/$(PROJ_NAME)_Pwr_Os.elf


