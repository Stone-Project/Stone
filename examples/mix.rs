// stone:job stone:math.mix
// stone:function mix_rs

#[no_mangle]
pub extern "C" fn mix_rs(a: f64, b: f64, t: f64) -> f64 {
    a + (b - a) * t
}
