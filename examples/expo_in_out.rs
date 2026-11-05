// stone:job stone:math.expo_in_out
// stone:function expo_in_out_rs

#[no_mangle]
pub extern "C" fn expo_in_out_rs(t: f64) -> f64 {
    if t == 0.0 { 0.0 }
    else if t == 1.0 { 1.0 }
    else if t < 0.5 { 0.5 * 2.0_f64.powf(20.0 * t - 10.0) }
    else { 1.0 - 0.5 * 2.0_f64.powf(-20.0 * t + 10.0) }
}
