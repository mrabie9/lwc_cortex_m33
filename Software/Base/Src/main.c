/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"


/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "data.h"
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
// #include <crypto_aead.h>
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */
static GPIO_InitTypeDef  GPIO_InitStruct;
/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
// #define ENCRYPT(a, b, c, d, e, f, g, h, i) crypto_aead_encrypt(a, b, c, d, e, f, g, h, i)
// #define DECRYPT(a, b, c, d, e, f, g, h, i) crypto_aead_decrypt(a, b, c, d, e, f, g, h, i)

#define MSG_SIZE_B INPUT_SIZE*4 // message size in bytes
#define MSG_SIZE_INT INPUT_SIZE // num of ints in message

// #define POWER_CONS
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

COM_InitTypeDef BspCOMInit;

UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void SystemPower_Config(void);
static void MX_GPIO_Init(void);
static void MX_ICACHE_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
/* DWT (Data Watchpoint and Trace) registers, only exists on ARM Cortex with a DWT unit */
#define KIN1_DWT_CONTROL (*((volatile uint32_t *)0xE0001000))
/*!< DWT Control register */
#define KIN1_DWT_CYCCNTENA_BIT (1UL << 0)
/*!< CYCCNTENA bit in DWT_CONTROL register */
#define KIN1_DWT_CYCCNT (*((volatile uint32_t *)0xE0001004))
/*!< DWT Cycle Counter register */
#define KIN1_DEMCR (*((volatile uint32_t *)0xE000EDFC))
/*!< DEMCR: Debug Exception and Monitor Control Register */
#define KIN1_LAR (*((volatile uint32_t *)0xE0001FB0))
/*!< lock access register */
#define KIN1_TRCENA_BIT (1UL << 24)
/*!< Trace enable bit in DEMCR register */

#define KIN1_InitCycleCounter() \
  KIN1_DEMCR |= KIN1_TRCENA_BIT
/*!< TRCENA: Enable trace and debug block DEMCR (Debug Exception and Monitor Control Register */

#define KIN1_EnableLockAccess() \
  KIN1_LAR = 0xC5ACCE55;
/*!< lock access */

#define KIN1_ResetCycleCounter() \
  KIN1_DWT_CYCCNT = 0
/*!< Reset cycle counter */

#define KIN1_EnableCycleCounter() \
  KIN1_DWT_CONTROL |= KIN1_DWT_CYCCNTENA_BIT
/*!< Enable cycle counter */

#define KIN1_DisableCycleCounter() \
  KIN1_DWT_CONTROL &= ~KIN1_DWT_CYCCNTENA_BIT
/*!< Disable cycle counter */

#define KIN1_GetCycleCounter() \
  KIN1_DWT_CYCCNT
/*!< Read cycle counter register */

void send_serial(uint8_t *data, int size)
{

  HAL_UART_Transmit(&huart2, data, size, HAL_MAX_DELAY);
}

void receive_serial(uint8_t *data, int size)
{

  HAL_UART_Receive(&huart2, data, size, HAL_MAX_DELAY);
}

// Sync controller and wrapper
void sync()
{
  float zero = 0.0;
  float one = 1.0;
  uint8_t size = sizeof(float);

  // Sync
  float val;
  receive_serial(&val, size);
  if (val == (float)0)
  {
    send_serial(&zero, size);
  }
  else
  {
    send_serial(&one, size);
  }
}

uint32_t cycles_e, cycles_d;  /* number of cycles */
int freq;

void send_app_runtime(float c)
{
  float time = (float)c / freq; 
  uint8_t size = sizeof(float);

  // Sync with script
  sync();
  // Send app runtime (seconds)
  send_serial(&time, size);
}

void send_runtime(float c)
{
  uint8_t size = sizeof(float);
  float time = (float)c / freq; 

  // Sync with script
  sync();
  send_serial(&time, size);
}

void send_output(double output)
{
  uint8_t size = sizeof(double);

  // Sync with script
  sync();
  send_serial(&output, size);
}

void send_uint32(uint32_t output)
{
  uint8_t size = sizeof(uint32_t);

  // Sync with script
  sync();
  send_serial(&output, size);
}
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{

  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* Configure the System Power */
  SystemPower_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_ICACHE_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */
 LED1_GPIO_CLK_ENABLE();
 LED2_GPIO_CLK_ENABLE();
 LED3_GPIO_CLK_ENABLE();

 /* -2- Configure IO in output push-pull mode to drive external LEDs */
 GPIO_InitStruct.Mode  = GPIO_MODE_OUTPUT_PP;
 GPIO_InitStruct.Pull  = GPIO_NOPULL;
 GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;

 GPIO_InitStruct.Pin = LED1_PIN;
 HAL_GPIO_Init(LED1_GPIO_PORT, &GPIO_InitStruct);
 GPIO_InitStruct.Pin = LED2_PIN;
 HAL_GPIO_Init(LED2_GPIO_PORT, &GPIO_InitStruct);
 GPIO_InitStruct.Pin = LED3_PIN;
 HAL_GPIO_Init(LED3_GPIO_PORT, &GPIO_InitStruct);

  /* USER CODE END 2 */

  /* Initialize COM1 port (115200, 8 bits (7-bit data + 1 stop bit), no parity */
  BspCOMInit.BaudRate   = 115200;
  BspCOMInit.WordLength = COM_WORDLENGTH_8B;
  BspCOMInit.StopBits   = COM_STOPBITS_1;
  BspCOMInit.Parity     = COM_PARITY_NONE;
  BspCOMInit.HwFlowCtl  = COM_HWCONTROL_NONE;
  if (BSP_COM_Init(COM1, &BspCOMInit) != BSP_ERROR_NONE)
  {
    Error_Handler();
  }

  KIN1_InitCycleCounter(); /* enable DWT hardware */
  KIN1_EnableLockAccess();
  freq = HAL_RCC_GetHCLKFreq();
  
// #if CRYPTO_KEYBYTES==16
//     volatile unsigned char key[CRYPTO_KEYBYTES] = {0xDEADBEEF, 0x01234567, 0x89ABCDEF, 0xDEADBEEF};
// #else 
//     volatile unsigned char  key[CRYPTO_KEYBYTES] = {0xDEADBEEF, 0x01234567, 0x89ABCDEF, 0xDEADBEEF, 0xDEADBEEF, 0x01234567, 0x89ABCDEF, 0xDEADBEEF};
// #endif
//   volatile unsigned char nonce[CRYPTO_NPUBBYTES] = {0};
//   // volatile unsigned char key[CRYPTO_KEYBYTES] = {0};
//   volatile uint64_t msglen = MSG_SIZE_B;// sizeof(text) / sizeof(unsigned char);
//   volatile unsigned long long ctlen = 0;
//   volatile unsigned char ct[MSG_SIZE_B + CRYPTO_ABYTES] = {0};
//   volatile unsigned long long adlen = 0;

//   // decrypt check
  uint8_t dt[MSG_SIZE_B] = {0};

//   // Declare pointers
//   volatile unsigned char *c;
//   volatile unsigned long long *clen;
//   volatile uint64_t *mlen;
//   volatile unsigned char *k, *npub;
//   volatile unsigned char *m;

//   // Initialise pointers
//   k = key;
//   npub = nonce;
//   clen = &ctlen;
//   m = text;
//   c = ct;
//   mlen = &msglen;
	
  double output;
  uint8_t sum = 0;
  uint32_t err_c = 0;

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
#ifdef POWER_CONS
    // Sync before app execution
    // HAL_Delay(10000);
		// sync();
    float discard1, discard2, discard3;
    double encrypt, decrypt;
    HAL_GPIO_TogglePin(LED1_GPIO_PORT, LED1_PIN);
    HAL_GPIO_TogglePin(LED2_GPIO_PORT, LED2_PIN);
    HAL_GPIO_TogglePin(LED3_GPIO_PORT, LED3_PIN);
    // HAL_Delay(3000);
    HAL_UART_Receive(&huart2, &discard1, 4, 2000);
    HAL_GPIO_TogglePin(LED1_GPIO_PORT, LED1_PIN);
    HAL_GPIO_TogglePin(LED2_GPIO_PORT, LED2_PIN);
    HAL_GPIO_TogglePin(LED3_GPIO_PORT, LED3_PIN);
    // KIN1_ResetCycleCounter();  /* reset cycle counter */
		// KIN1_EnableCycleCounter(); /* start counting */
    
		for(int i=0;i<N_LOOP;i++)
			encrypt = ENCRYPT(c, clen, m, msglen, NULL, adlen, NULL, npub, k);
    // cycles_e = KIN1_GetCycleCounter(); /* get cycle counter */
    // KIN1_ResetCycleCounter();  /* reset cycle counter */
		// KIN1_EnableCycleCounter(); /* start counting */
    HAL_GPIO_TogglePin(LED1_GPIO_PORT, LED1_PIN);
    HAL_GPIO_TogglePin(LED2_GPIO_PORT, LED2_PIN);
    HAL_GPIO_TogglePin(LED3_GPIO_PORT, LED3_PIN);
    // HAL_Delay(3000);
    HAL_UART_Receive(&huart2, &discard2, 4, 3000);
    HAL_GPIO_TogglePin(LED1_GPIO_PORT, LED1_PIN);
    HAL_GPIO_TogglePin(LED2_GPIO_PORT, LED2_PIN);
    HAL_GPIO_TogglePin(LED3_GPIO_PORT, LED3_PIN);

		for(int i=0;i<N_LOOP;i++)
		  decrypt = DECRYPT(dt, mlen, NULL, c, *clen, NULL, adlen, npub, k);
    // cycles_d = KIN1_GetCycleCounter(); /* get cycle counter */
    HAL_GPIO_TogglePin(LED1_GPIO_PORT, LED1_PIN);
    HAL_GPIO_TogglePin(LED2_GPIO_PORT, LED2_PIN);
    HAL_GPIO_TogglePin(LED3_GPIO_PORT, LED3_PIN);
    // HAL_Delay(2000);
    HAL_UART_Receive(&huart2, &discard3, 4, 3000);
    HAL_GPIO_TogglePin(LED1_GPIO_PORT, LED1_PIN);
    HAL_GPIO_TogglePin(LED2_GPIO_PORT, LED2_PIN);
    HAL_GPIO_TogglePin(LED3_GPIO_PORT, LED3_PIN);  
    
    // Checksum
    // uint32_t dt_int;
    // for (int i=0;i<MSG_SIZE_INT;i++){
    //   dt_int = dt[i*4] | (dt[i*4 + 1] << 8) | (dt[i*4 +2] << 16) | (dt[i*4 +3] << 24);
    //   if (dt_int != text[i])
    //     err_c += 1;
    // }
    
    
    // Send data
		send_app_runtime(cycles_e);
    send_serial(&discard1, 4);
    send_serial(&discard2, 4);
    send_serial(&discard3, 4);
    send_runtime(cycles_d);
    send_output(encrypt);
		send_output(decrypt);
    send_uint32(err_c);
	

	#else
    float discard;
		// Sync before app execution
		sync();

		KIN1_ResetCycleCounter();  /* reset cycle counter */
		KIN1_EnableCycleCounter(); /* start counting */
    
		// Start application
    // Encryption
		double encrypt = 0;//ENCRYPT(c, clen, m, msglen, NULL, adlen, NULL, npub, k);
		cycles_e = KIN1_GetCycleCounter(); /* get cycle counter */
    
    // Decryption
    KIN1_ResetCycleCounter();  /* reset cycle counter */
		KIN1_EnableCycleCounter(); /* start counting */
    // DECRYPT(dm, mlen, NULL, c, ctlen, NULL, adlen, npub, k);
    double decrypt = 0;//DECRYPT(dt, mlen, NULL, c, *clen, NULL, adlen, npub, k);

    cycles_d = KIN1_GetCycleCounter(); /* get cycle counter */

    send_serial(&discard, 4);

    // Checksum
    uint32_t dt_int;
    for (int i=0;i<MSG_SIZE_INT;i++){
      dt_int = dt[i*4] | (dt[i*4 + 1] << 8) | (dt[i*4 +2] << 16) | (dt[i*4 +3] << 24);
      if (dt_int != text[i])
        err_c += 1;
    }

    send_serial(&discard, 4);
    // Send data
		send_app_runtime(cycles_e);
    send_runtime(cycles_d);
    send_output(encrypt);
		send_output(decrypt);
    send_uint32(0);
    send_uint32(text);
	
	#endif
  }
   KIN1_DisableCycleCounter();
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  if (HAL_PWREx_ControlVoltageScaling(PWR_REGULATOR_VOLTAGE_SCALE1) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_MSI;
  RCC_OscInitStruct.MSIState = RCC_MSI_ON;
  RCC_OscInitStruct.MSICalibrationValue = RCC_MSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.MSIClockRange = RCC_MSIRANGE_0;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_MSI;
  RCC_OscInitStruct.PLL.PLLMBOOST = RCC_PLLMBOOST_DIV4;
  RCC_OscInitStruct.PLL.PLLM = 3;
  RCC_OscInitStruct.PLL.PLLN = 10;
  RCC_OscInitStruct.PLL.PLLP = 8;
  RCC_OscInitStruct.PLL.PLLQ = 2;
  RCC_OscInitStruct.PLL.PLLR = 1;
  RCC_OscInitStruct.PLL.PLLRGE = RCC_PLLVCIRANGE_1;
  RCC_OscInitStruct.PLL.PLLFRACN = 0;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2
                              |RCC_CLOCKTYPE_PCLK3;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB3CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_4) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief Power Configuration
  * @retval None
  */
static void SystemPower_Config(void)
{
  HAL_PWREx_EnableVddIO2();

  /*
   * Disable the internal Pull-Up in Dead Battery pins of UCPD peripheral
   */
  HAL_PWREx_DisableUCPDDeadBattery();

  /*
   * Switch to SMPS regulator instead of LDO
   */
  if (HAL_PWREx_ConfigSupply(PWR_SMPS_SUPPLY) != HAL_OK)
  {
    Error_Handler();
  }
/* USER CODE BEGIN PWR */
/* USER CODE END PWR */
}

/**
  * @brief ICACHE Initialization Function
  * @param None
  * @retval None
  */
static void MX_ICACHE_Init(void)
{

  /* USER CODE BEGIN ICACHE_Init 0 */

  /* USER CODE END ICACHE_Init 0 */

  /* USER CODE BEGIN ICACHE_Init 1 */

  /* USER CODE END ICACHE_Init 1 */

  /** Enable instruction cache in 1-way (direct mapped cache)
  */
  if (HAL_ICACHE_ConfigAssociativityMode(ICACHE_1WAY) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_ICACHE_Enable() != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN ICACHE_Init 2 */

  /* USER CODE END ICACHE_Init 2 */

}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART1;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  huart2.Init.OneBitSampling = UART_ONE_BIT_SAMPLE_DISABLE;
  huart2.Init.ClockPrescaler = UART_PRESCALER_DIV1;
  huart2.AdvancedInit.AdvFeatureInit = UART_ADVFEATURE_NO_INIT;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_UARTEx_SetTxFifoThreshold(&huart2, UART_TXFIFO_THRESHOLD_1_8) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_UARTEx_SetRxFifoThreshold(&huart2, UART_RXFIFO_THRESHOLD_1_8) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_UARTEx_DisableFifoMode(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
/* USER CODE BEGIN MX_GPIO_Init_1 */
/* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();
  __HAL_RCC_GPIOG_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, UCPD_DBn_Pin|LED_BLUE_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : PC13 */
  GPIO_InitStruct.Pin = GPIO_PIN_13;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /*Configure GPIO pin : VBUS_SENSE_Pin */
  GPIO_InitStruct.Pin = VBUS_SENSE_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(VBUS_SENSE_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : UCPD_FLT_Pin */
  GPIO_InitStruct.Pin = UCPD_FLT_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(UCPD_FLT_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : PB15 */
  GPIO_InitStruct.Pin = GPIO_PIN_15;
  GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pin : LED_RED_Pin */
  GPIO_InitStruct.Pin = LED_RED_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(LED_RED_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : LED_GREEN_Pin */
  GPIO_InitStruct.Pin = LED_GREEN_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(LED_GREEN_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : PA9 PA10 */
  GPIO_InitStruct.Pin = GPIO_PIN_9|GPIO_PIN_10;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF7_USART1;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : PA11 PA12 */
  GPIO_InitStruct.Pin = GPIO_PIN_11|GPIO_PIN_12;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pin : PA15 */
  GPIO_InitStruct.Pin = GPIO_PIN_15;
  GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : UCPD_DBn_Pin LED_BLUE_Pin */
  GPIO_InitStruct.Pin = UCPD_DBn_Pin|LED_BLUE_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

/* USER CODE BEGIN MX_GPIO_Init_2 */
/* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
