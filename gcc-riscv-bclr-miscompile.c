#include <stdint.h>
#include <stdio.h>
#include <strings.h>

/*
 * GCC RISC-V bclr_lowest_set_bit wrong-code reproducer.
 *
 * Reproduce with openRuyi GCC 16.2.0:
 *   gcc-16 -O2 -march=rva23u64 -o bitloop gcc-riscv-bclr-miscompile.c
 *   ./bitloop
 *
 * Expected output: 0xffff
 * Affected compiler output: 0x2aab
 *
 * Disable the faulty RTL pass:
 *   gcc-16 -O2 -march=rva23u64 \
 *     -fdisable-rtl-bclr_lowest_set_bit \
 *     -o bitloop-fixed gcc-riscv-bclr-miscompile.c
 *   ./bitloop-fixed
 *
 * Expected fixed output: 0xffff
 */

__attribute__((noinline)) unsigned
scan(uint16_t mask)
{
    unsigned result = 0;

    for (uint32_t dword = mask, bit;
         ((bit = ffs(dword) - 1), dword);
         dword &= dword - 1)
        result |= 1u << bit;

    return result;
}

int
main(void)
{
    const unsigned expected = 0xffff;
    const unsigned actual = scan(expected);

    printf("%#x\n", actual);
    return actual != expected;
}
