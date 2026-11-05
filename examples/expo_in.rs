// stone:job stone:math.expo_in
// stone:function expo_in_rs

#[no_mangle]
pub extern "C" fn expo_in_rs(t: f64) -> f64 {
    if t == 0.0 { 0.0 } else { 2.0_f64.powf(10.0 * (t - 1.0)) }
}
