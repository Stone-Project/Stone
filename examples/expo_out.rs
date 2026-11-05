// stone:job stone:math.expo_out
// stone:function expo_out_rs

#[no_mangle]
pub extern "C" fn expo_out_rs(t: f64) -> f64 {
    if t == 1.0 { 1.0 } else { 1.0 - 2.0_f64.powf(-10.0 * t) }
}
