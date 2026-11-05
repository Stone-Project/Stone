// stone:job stone:math.back_in
// stone:function back_in_rs

#[no_mangle]
pub extern "C" fn back_in_rs(t: f64) -> f64 {
    t * t * (2.70158 * t - 1.70158)
}
