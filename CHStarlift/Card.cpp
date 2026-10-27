// STARLIFT.DAT (Card.h): block 0 holds "STARLIFT" and the build's hash (CardIndex.h, written with the file by
// tools/make_card.py), so a card from another build is refused; then the picture section, then the song section.
// Four 512 B slots keep the blocks used last: the pictures on screen are read once and drawn from RAM after that.
#include <CHGame.h>
#include <Fat.h>
#include "Card.h"
#include "CardIndex.h"

namespace card {

enum { SLOTS = 4 };
alignas(4) static uint8_t buf[SLOTS][512];
static uint16_t tag[SLOTS] = { 0xffff, 0xffff, 0xffff, 0xffff };
static uint8_t age[SLOTS], tick;                  // the least recently used slot is the one to replace
static fat::Run runs[4];
static uint8_t nRuns;
static bool open_;

bool open() {
    for (uint8_t i = 0; i < SLOTS; i++) tag[i] = 0xffff;
    nRuns = fat::open("STARLIFTDAT", runs, 4, buf[0]);
    open_ = nRuns && fat::read(runs, nRuns, 0, buf[0]) && !memcmp(buf[0], "STARLIFT", 8) && !memcmp(buf[0] + 8, &CARD_HASH, 4);
    return open_;
}

bool ok() { return open_; }

const uint8_t *at(uint32_t off) {
    if (!open_) return nullptr;
    const uint16_t blk = (uint16_t)(off >> 9);
    for (uint8_t i = 0; i < SLOTS; i++) if (tag[i] == blk) { age[i] = ++tick; return buf[i] + (off & 511); }
    uint8_t v = 0;
    for (uint8_t i = 1; i < SLOTS; i++) if ((uint8_t)(tick - age[i]) > (uint8_t)(tick - age[v])) v = i;
    tag[v] = 0xffff;
    if (!fat::read(runs, nRuns, blk, buf[v])) { open_ = false; return nullptr; }
    tag[v] = blk;
    age[v] = ++tick;
    return buf[v] + (off & 511);
}

bool copy(uint8_t *dst, uint32_t off, uint16_t n) {
    while (n) {
        const uint8_t *s = at(off);
        if (!s) return false;
        uint16_t k = (uint16_t)(512 - (off & 511));
        if (k > n) k = n;
        memcpy(dst, s, k);
        dst += k; off += k; n -= k;
    }
    return true;
}

}  // namespace card
